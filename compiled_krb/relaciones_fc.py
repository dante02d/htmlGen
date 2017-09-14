# relaciones_fc.py

from __future__ import with_statement
from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def item(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('parejas', 'item', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('parejas', 'render',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),
                        rule.pattern(2).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('relaciones')
  
  fc_rule.fc_rule('item', This_rule_base, item,
    (('parejas', 'item',
      (contexts.variable('itemName'),
       contexts.variable('itemParams'),
       contexts.variable('itemText'),),
      False),),
    (contexts.variable('itemName'),
     contexts.variable('itemParams'),
     pattern.pattern_literal('itemText'),))


Krb_filename = '../relaciones.krb'
Krb_lineno_map = (
    ((13, 17), (3, 3)),
    ((18, 21), (5, 5)),
)
