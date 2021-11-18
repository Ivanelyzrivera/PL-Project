
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ARITY ASSIGN CHARACTER COMMA CONS CONSQ DIGIT DIVIDE ELSE EMPTY EMPTYQ EQ FALSE FIRST FUNQ GEQ GT IF IN LB LEQ LET LISTQ LP LT MAP MINUS NEQ NUMQ OR PLUS RB REST RP SC THEN TILDE TIMES TO TRUEmainexplist : explist\n\t\t           | emptyexplist : exp\n               | exp COMMA explistexp : term\n           | term binop exp\n           | IF exp THEN exp ELSE exp\n           | LET def IN exp\n           | MAP idlist TO expterm : unop term\n            | factor\n            | factor LP mainexplist RP\n            | empty\n            | int\n\t        | string\n            | boolfactor   : LP exp RP\n                | prim\n                | id\n\t\t        | stringdef  : id ASSIGN exp SC\n                | id ASSIGN exp SC defidlist   : propidlist\n                | emptypropidlist   : id\n                    | id COMMA propidlistbool : TRUE\n            | FALSEunop : sign\n            | TILDE binop    : sign\n                | TIMES\n                | DIVIDE\n                | EQ\n                | NEQ\n                | LT\n                | GT\n                | LEQ\n                | GEQ\n                | AND\n                | OR sign : PLUS\n            | MINUS prim : NUMQ\n            | FUNQ\n            | LISTQ\n            | EMPTYQ\n            | CONSQ\n            | CONS\n            | FIRST\n            | REST\n            | ARITYid   :\n            | id\n            | int\n            | int id\n            | string\n            | string idint  : DIGIT\n            | DIGIT intstring : CHARACTER\n              | CHARACTER stringempty :\n             | EMPTY'
    
_lr_action_items = {'$end':([0,1,2,3,4,5,6,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,49,52,53,58,61,62,63,64,65,66,68,70,73,75,77,79,80,82,],[-53,0,-1,-2,-3,-64,-5,-53,-11,-14,-15,-16,-29,-30,-18,-19,-59,-61,-27,-28,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-53,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-13,-53,-53,-10,-54,-54,-60,-62,-4,-6,-53,-53,-17,-8,-9,-12,-53,-7,]),'TIMES':([0,3,5,6,7,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,49,52,53,58,59,61,62,63,64,67,68,69,70,73,79,80,],[-53,-13,-64,38,-53,-53,-11,-53,-14,-15,-16,-29,-30,-18,-19,-59,-61,-27,-28,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-53,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-13,-53,-53,-10,-53,-54,-54,-60,-62,-53,-53,-53,-53,-17,-12,-53,]),'DIVIDE':([0,3,5,6,7,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,49,52,53,58,59,61,62,63,64,67,68,69,70,73,79,80,],[-53,-13,-64,39,-53,-53,-11,-53,-14,-15,-16,-29,-30,-18,-19,-59,-61,-27,-28,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-53,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-13,-53,-53,-10,-53,-54,-54,-60,-62,-53,-53,-53,-53,-17,-12,-53,]),'EQ':([0,3,5,6,7,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,49,52,53,58,59,61,62,63,64,67,68,69,70,73,79,80,],[-53,-13,-64,40,-53,-53,-11,-53,-14,-15,-16,-29,-30,-18,-19,-59,-61,-27,-28,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-53,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-13,-53,-53,-10,-53,-54,-54,-60,-62,-53,-53,-53,-53,-17,-12,-53,]),'NEQ':([0,3,5,6,7,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,49,52,53,58,59,61,62,63,64,67,68,69,70,73,79,80,],[-53,-13,-64,41,-53,-53,-11,-53,-14,-15,-16,-29,-30,-18,-19,-59,-61,-27,-28,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-53,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-13,-53,-53,-10,-53,-54,-54,-60,-62,-53,-53,-53,-53,-17,-12,-53,]),'LT':([0,3,5,6,7,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,49,52,53,58,59,61,62,63,64,67,68,69,70,73,79,80,],[-53,-13,-64,42,-53,-53,-11,-53,-14,-15,-16,-29,-30,-18,-19,-59,-61,-27,-28,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-53,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-13,-53,-53,-10,-53,-54,-54,-60,-62,-53,-53,-53,-53,-17,-12,-53,]),'GT':([0,3,5,6,7,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,49,52,53,58,59,61,62,63,64,67,68,69,70,73,79,80,],[-53,-13,-64,43,-53,-53,-11,-53,-14,-15,-16,-29,-30,-18,-19,-59,-61,-27,-28,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-53,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-13,-53,-53,-10,-53,-54,-54,-60,-62,-53,-53,-53,-53,-17,-12,-53,]),'LEQ':([0,3,5,6,7,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,49,52,53,58,59,61,62,63,64,67,68,69,70,73,79,80,],[-53,-13,-64,44,-53,-53,-11,-53,-14,-15,-16,-29,-30,-18,-19,-59,-61,-27,-28,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-53,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-13,-53,-53,-10,-53,-54,-54,-60,-62,-53,-53,-53,-53,-17,-12,-53,]),'GEQ':([0,3,5,6,7,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,49,52,53,58,59,61,62,63,64,67,68,69,70,73,79,80,],[-53,-13,-64,45,-53,-53,-11,-53,-14,-15,-16,-29,-30,-18,-19,-59,-61,-27,-28,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-53,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-13,-53,-53,-10,-53,-54,-54,-60,-62,-53,-53,-53,-53,-17,-12,-53,]),'AND':([0,3,5,6,7,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,49,52,53,58,59,61,62,63,64,67,68,69,70,73,79,80,],[-53,-13,-64,46,-53,-53,-11,-53,-14,-15,-16,-29,-30,-18,-19,-59,-61,-27,-28,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-53,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-13,-53,-53,-10,-53,-54,-54,-60,-62,-53,-53,-53,-53,-17,-12,-53,]),'OR':([0,3,5,6,7,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,49,52,53,58,59,61,62,63,64,67,68,69,70,73,79,80,],[-53,-13,-64,47,-53,-53,-11,-53,-14,-15,-16,-29,-30,-18,-19,-59,-61,-27,-28,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-53,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-13,-53,-53,-10,-53,-54,-54,-60,-62,-53,-53,-53,-53,-17,-12,-53,]),'PLUS':([0,3,5,6,7,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,49,52,53,58,59,61,62,63,64,67,68,69,70,73,79,80,],[24,-13,-64,24,24,24,-11,24,-14,-15,-16,-29,-30,-18,-19,-59,-61,-27,-28,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,24,24,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-13,-53,-53,-10,24,-54,-54,-60,-62,24,24,24,24,-17,-12,24,]),'MINUS':([0,3,5,6,7,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,49,52,53,58,59,61,62,63,64,67,68,69,70,73,79,80,],[25,-13,-64,25,25,25,-11,25,-14,-15,-16,-29,-30,-18,-19,-59,-61,-27,-28,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,25,25,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-13,-53,-53,-10,25,-54,-54,-60,-62,25,25,25,25,-17,-12,25,]),'COMMA':([0,3,4,5,6,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,49,52,53,57,58,59,61,62,63,64,66,68,70,71,73,75,77,79,80,82,],[-53,-13,35,-64,-5,-53,-53,-11,-14,-15,-16,-29,-30,-18,-19,-59,-61,-27,-28,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-53,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-13,-53,-53,71,-10,-53,-54,-54,-60,-62,-6,-53,-53,-53,-17,-8,-9,-12,-53,-7,]),'EMPTY':([0,7,9,10,12,16,17,24,25,35,36,37,38,39,40,41,42,43,44,45,46,47,59,67,68,69,70,80,],[5,5,5,5,5,-29,-30,-42,-43,5,5,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,5,5,5,5,5,5,]),'IF':([0,7,12,24,25,35,36,37,38,39,40,41,42,43,44,45,46,47,59,67,68,69,70,80,],[7,7,7,-42,-43,7,7,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,7,7,7,7,7,7,]),'LET':([0,7,12,24,25,35,36,37,38,39,40,41,42,43,44,45,46,47,59,67,68,69,70,80,],[8,8,8,-42,-43,8,8,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,8,8,8,8,8,8,]),'MAP':([0,7,12,24,25,35,36,37,38,39,40,41,42,43,44,45,46,47,59,67,68,69,70,80,],[9,9,9,-42,-43,9,9,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,9,9,9,9,9,9,]),'TILDE':([0,7,10,12,16,17,24,25,35,36,37,38,39,40,41,42,43,44,45,46,47,59,67,68,69,70,80,],[17,17,17,17,-29,-30,-42,-43,17,17,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,17,17,17,17,17,17,]),'LP':([0,7,10,11,12,13,14,16,17,18,19,20,21,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,52,53,59,61,62,63,64,67,68,69,70,73,80,],[12,12,12,59,12,-53,-20,-29,-30,-18,-19,-59,-61,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,12,12,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-53,-53,12,-54,-54,-60,-62,12,12,12,12,-17,12,]),'DIGIT':([0,7,8,9,10,12,13,14,16,17,20,21,24,25,35,36,37,38,39,40,41,42,43,44,45,46,47,52,53,59,63,64,67,68,69,70,71,80,81,],[20,20,20,20,20,20,20,20,-29,-30,20,-61,-42,-43,20,20,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,20,20,20,-60,-62,20,20,20,20,20,20,20,]),'CHARACTER':([0,7,8,9,10,12,13,14,16,17,20,21,24,25,35,36,37,38,39,40,41,42,43,44,45,46,47,52,53,59,63,64,67,68,69,70,71,80,81,],[21,21,21,21,21,21,21,21,-29,-30,-59,21,-42,-43,21,21,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,21,21,21,-60,-62,21,21,21,21,21,21,21,]),'TRUE':([0,7,10,12,16,17,24,25,35,36,37,38,39,40,41,42,43,44,45,46,47,59,67,68,69,70,80,],[22,22,22,22,-29,-30,-42,-43,22,22,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,22,22,22,22,22,22,]),'FALSE':([0,7,10,12,16,17,24,25,35,36,37,38,39,40,41,42,43,44,45,46,47,59,67,68,69,70,80,],[23,23,23,23,-29,-30,-42,-43,23,23,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,23,23,23,23,23,23,]),'NUMQ':([0,7,10,12,16,17,24,25,35,36,37,38,39,40,41,42,43,44,45,46,47,59,67,68,69,70,80,],[26,26,26,26,-29,-30,-42,-43,26,26,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,26,26,26,26,26,26,]),'FUNQ':([0,7,10,12,16,17,24,25,35,36,37,38,39,40,41,42,43,44,45,46,47,59,67,68,69,70,80,],[27,27,27,27,-29,-30,-42,-43,27,27,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,27,27,27,27,27,27,]),'LISTQ':([0,7,10,12,16,17,24,25,35,36,37,38,39,40,41,42,43,44,45,46,47,59,67,68,69,70,80,],[28,28,28,28,-29,-30,-42,-43,28,28,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,28,28,28,28,28,28,]),'EMPTYQ':([0,7,10,12,16,17,24,25,35,36,37,38,39,40,41,42,43,44,45,46,47,59,67,68,69,70,80,],[29,29,29,29,-29,-30,-42,-43,29,29,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,29,29,29,29,29,29,]),'CONSQ':([0,7,10,12,16,17,24,25,35,36,37,38,39,40,41,42,43,44,45,46,47,59,67,68,69,70,80,],[30,30,30,30,-29,-30,-42,-43,30,30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,30,30,30,30,30,30,]),'CONS':([0,7,10,12,16,17,24,25,35,36,37,38,39,40,41,42,43,44,45,46,47,59,67,68,69,70,80,],[31,31,31,31,-29,-30,-42,-43,31,31,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,31,31,31,31,31,31,]),'FIRST':([0,7,10,12,16,17,24,25,35,36,37,38,39,40,41,42,43,44,45,46,47,59,67,68,69,70,80,],[32,32,32,32,-29,-30,-42,-43,32,32,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,32,32,32,32,32,32,]),'REST':([0,7,10,12,16,17,24,25,35,36,37,38,39,40,41,42,43,44,45,46,47,59,67,68,69,70,80,],[33,33,33,33,-29,-30,-42,-43,33,33,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,33,33,33,33,33,33,]),'ARITY':([0,7,10,12,16,17,24,25,35,36,37,38,39,40,41,42,43,44,45,46,47,59,67,68,69,70,80,],[34,34,34,34,-29,-30,-42,-43,34,34,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,34,34,34,34,34,34,]),'RP':([2,3,4,5,6,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,49,52,53,58,59,60,61,62,63,64,65,66,68,70,72,73,75,77,79,80,82,],[-1,-2,-3,-64,-5,-53,-11,-53,-14,-15,-16,-29,-30,-18,-19,-59,-61,-27,-28,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-53,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-13,-53,-53,-10,-53,73,-54,-54,-60,-62,-4,-6,-53,-53,79,-17,-8,-9,-12,-53,-7,]),'THEN':([5,6,7,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,49,52,53,58,61,62,63,64,66,68,70,73,75,77,79,80,82,],[-64,-5,-53,-53,-11,-14,-15,-16,-29,-30,-18,-19,-59,-61,-27,-28,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,67,-13,-53,-53,-10,-54,-54,-60,-62,-6,-53,-53,-17,-8,-9,-12,-53,-7,]),'TO':([5,9,20,21,52,53,54,55,56,57,61,62,63,64,71,78,],[-64,-53,-59,-61,-53,-53,70,-23,-24,-25,-54,-54,-60,-62,-53,-26,]),'ELSE':([5,6,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,36,37,38,39,40,41,42,43,44,45,46,47,49,52,53,58,61,62,63,64,66,67,68,70,73,74,75,77,79,80,82,],[-64,-5,-53,-11,-14,-15,-16,-29,-30,-18,-19,-59,-61,-27,-28,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-13,-53,-53,-10,-54,-54,-60,-62,-6,-53,-53,-53,-17,80,-8,-9,-12,-53,-7,]),'SC':([5,6,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,36,37,38,39,40,41,42,43,44,45,46,47,49,52,53,58,61,62,63,64,66,68,69,70,73,75,76,77,79,80,82,],[-64,-5,-53,-11,-14,-15,-16,-29,-30,-18,-19,-59,-61,-27,-28,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-13,-53,-53,-10,-54,-54,-60,-62,-6,-53,-53,-53,-17,-8,81,-9,-12,-53,-7,]),'ASSIGN':([8,20,21,51,52,53,61,62,63,64,81,],[-53,-59,-61,69,-53,-53,-54,-54,-60,-62,-53,]),'IN':([50,81,83,],[68,-21,-22,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'mainexplist':([0,59,],[1,72,]),'explist':([0,35,59,],[2,65,2,]),'empty':([0,7,9,10,12,35,36,59,67,68,69,70,80,],[3,49,56,49,49,49,49,3,49,49,49,49,49,]),'exp':([0,7,12,35,36,59,67,68,69,70,80,],[4,48,60,4,66,4,74,75,76,77,82,]),'term':([0,7,10,12,35,36,59,67,68,69,70,80,],[6,6,58,6,6,6,6,6,6,6,6,6,]),'unop':([0,7,10,12,35,36,59,67,68,69,70,80,],[10,10,10,10,10,10,10,10,10,10,10,10,]),'factor':([0,7,10,12,35,36,59,67,68,69,70,80,],[11,11,11,11,11,11,11,11,11,11,11,11,]),'int':([0,7,8,9,10,12,13,14,20,35,36,52,53,59,67,68,69,70,71,80,81,],[13,13,52,52,13,13,52,52,63,13,13,52,52,13,13,13,13,13,52,13,52,]),'string':([0,7,8,9,10,12,13,14,21,35,36,52,53,59,67,68,69,70,71,80,81,],[14,14,53,53,14,14,53,53,64,14,14,53,53,14,14,14,14,14,53,14,53,]),'bool':([0,7,10,12,35,36,59,67,68,69,70,80,],[15,15,15,15,15,15,15,15,15,15,15,15,]),'sign':([0,6,7,10,12,35,36,59,67,68,69,70,80,],[16,37,16,16,16,16,16,16,16,16,16,16,16,]),'prim':([0,7,10,12,35,36,59,67,68,69,70,80,],[18,18,18,18,18,18,18,18,18,18,18,18,]),'id':([0,7,8,9,10,12,13,14,35,36,52,53,59,67,68,69,70,71,80,81,],[19,19,51,57,19,19,61,62,19,19,61,62,19,19,19,19,19,57,19,51,]),'binop':([6,],[36,]),'def':([8,81,],[50,83,]),'idlist':([9,],[54,]),'propidlist':([9,71,],[55,78,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> mainexplist","S'",1,None,None,None),
  ('mainexplist -> explist','mainexplist',1,'p_mainexplist','syntax.py',8),
  ('mainexplist -> empty','mainexplist',1,'p_mainexplist','syntax.py',9),
  ('explist -> exp','explist',1,'p_explist','syntax.py',13),
  ('explist -> exp COMMA explist','explist',3,'p_explist','syntax.py',14),
  ('exp -> term','exp',1,'p_exp','syntax.py',18),
  ('exp -> term binop exp','exp',3,'p_exp','syntax.py',19),
  ('exp -> IF exp THEN exp ELSE exp','exp',6,'p_exp','syntax.py',20),
  ('exp -> LET def IN exp','exp',4,'p_exp','syntax.py',21),
  ('exp -> MAP idlist TO exp','exp',4,'p_exp','syntax.py',22),
  ('term -> unop term','term',2,'p_term','syntax.py',26),
  ('term -> factor','term',1,'p_term','syntax.py',27),
  ('term -> factor LP mainexplist RP','term',4,'p_term','syntax.py',28),
  ('term -> empty','term',1,'p_term','syntax.py',29),
  ('term -> int','term',1,'p_term','syntax.py',30),
  ('term -> string','term',1,'p_term','syntax.py',31),
  ('term -> bool','term',1,'p_term','syntax.py',32),
  ('factor -> LP exp RP','factor',3,'p_factor','syntax.py',36),
  ('factor -> prim','factor',1,'p_factor','syntax.py',37),
  ('factor -> id','factor',1,'p_factor','syntax.py',38),
  ('factor -> string','factor',1,'p_factor','syntax.py',39),
  ('def -> id ASSIGN exp SC','def',4,'p_def','syntax.py',43),
  ('def -> id ASSIGN exp SC def','def',5,'p_def','syntax.py',44),
  ('idlist -> propidlist','idlist',1,'p_idlist','syntax.py',48),
  ('idlist -> empty','idlist',1,'p_idlist','syntax.py',49),
  ('propidlist -> id','propidlist',1,'p_propidlist','syntax.py',53),
  ('propidlist -> id COMMA propidlist','propidlist',3,'p_propidlist','syntax.py',54),
  ('bool -> TRUE','bool',1,'p_bool','syntax.py',58),
  ('bool -> FALSE','bool',1,'p_bool','syntax.py',59),
  ('unop -> sign','unop',1,'p_unop','syntax.py',63),
  ('unop -> TILDE','unop',1,'p_unop','syntax.py',64),
  ('binop -> sign','binop',1,'p_binop','syntax.py',68),
  ('binop -> TIMES','binop',1,'p_binop','syntax.py',69),
  ('binop -> DIVIDE','binop',1,'p_binop','syntax.py',70),
  ('binop -> EQ','binop',1,'p_binop','syntax.py',71),
  ('binop -> NEQ','binop',1,'p_binop','syntax.py',72),
  ('binop -> LT','binop',1,'p_binop','syntax.py',73),
  ('binop -> GT','binop',1,'p_binop','syntax.py',74),
  ('binop -> LEQ','binop',1,'p_binop','syntax.py',75),
  ('binop -> GEQ','binop',1,'p_binop','syntax.py',76),
  ('binop -> AND','binop',1,'p_binop','syntax.py',77),
  ('binop -> OR','binop',1,'p_binop','syntax.py',78),
  ('sign -> PLUS','sign',1,'p_sign','syntax.py',82),
  ('sign -> MINUS','sign',1,'p_sign','syntax.py',83),
  ('prim -> NUMQ','prim',1,'p_prim','syntax.py',87),
  ('prim -> FUNQ','prim',1,'p_prim','syntax.py',88),
  ('prim -> LISTQ','prim',1,'p_prim','syntax.py',89),
  ('prim -> EMPTYQ','prim',1,'p_prim','syntax.py',90),
  ('prim -> CONSQ','prim',1,'p_prim','syntax.py',91),
  ('prim -> CONS','prim',1,'p_prim','syntax.py',92),
  ('prim -> FIRST','prim',1,'p_prim','syntax.py',93),
  ('prim -> REST','prim',1,'p_prim','syntax.py',94),
  ('prim -> ARITY','prim',1,'p_prim','syntax.py',95),
  ('id -> <empty>','id',0,'p_id','syntax.py',99),
  ('id -> id','id',1,'p_id','syntax.py',100),
  ('id -> int','id',1,'p_id','syntax.py',101),
  ('id -> int id','id',2,'p_id','syntax.py',102),
  ('id -> string','id',1,'p_id','syntax.py',103),
  ('id -> string id','id',2,'p_id','syntax.py',104),
  ('int -> DIGIT','int',1,'p_int','syntax.py',119),
  ('int -> DIGIT int','int',2,'p_int','syntax.py',120),
  ('string -> CHARACTER','string',1,'p_string','syntax.py',124),
  ('string -> CHARACTER string','string',2,'p_string','syntax.py',125),
  ('empty -> <empty>','empty',0,'p_empty','syntax.py',129),
  ('empty -> EMPTY','empty',1,'p_empty','syntax.py',130),
]
