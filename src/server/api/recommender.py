import redis
from django.conf import settings
from .models import LinearAlgebraExpression

r = redis.Redis(host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                db=settings.REDIS_DB)

class Recommender:
    def get_lalg_key(self, id):
        return f'expression:{id}:computed with'

    def expressions_computed(self, expressions):
        expression_ids = [p.id for p in expressions]
        for expression_id in expression_ids:
            for with_id in expression_ids:
                # get the other expressions computed with each expression
                if expression_id != with_id:
                    # increment score for expression computed together
                    r.zincrby(self.get_lalg_key(expression_id), 1, with_id)

    def suggest_expressions_for(self, expressions, max_results=6):
        expression_ids = [p.id for p in expressions]
        if len(expressions) == 1:
            suggestions = r.zrange(
                self.get_lalg_key(expression_ids[0]),
                0, 1, desc=True)[:max_results]

        else:
            # generate a temporary key
            flat_ids = ''.join([str(id) for id in expression_ids])
            tmp_key = f'tmp_{flat_ids}'
            keys = [self.get_lalg_key(id) for id in expression_ids]
            r.zunionstore(tmp_key, keys)
            r.zrem(tmp_key, *expression_ids)
            suggestions = r.zrange(tmp_key, 0, 1, desc=True)[:max_results]
            r.delete(tmp_key)

        suggested_expressions_ids = [int(id) for id in suggestions]
        suggested_expressions = list(LinearAlgebraExpression.objects.filter(id__in=suggested_expressions_ids))
        suggested_expressions.sort(key=lambda x: suggested_expressions_ids.index(x.id))
        return suggested_expressions
            
