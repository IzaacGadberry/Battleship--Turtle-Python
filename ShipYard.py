import turtle as t

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
# The Turtles

carrierP1 = t.Turtle()
carrierP1.hideturtle()
carrierP2 = t.Turtle()
carrierP2.hideturtle()
carrierP3 = t.Turtle()
carrierP3.hideturtle()
carrierP4 = t.Turtle()
carrierP4.hideturtle()
carrierP5 = t.Turtle()
carrierP5.hideturtle()

battleshipP1 = t.Turtle()
battleshipP1.hideturtle()
battleshipP2 = t.Turtle()
battleshipP2.hideturtle()
battleshipP3 = t.Turtle()
battleshipP3.hideturtle()
battleshipP4 = t.Turtle()
battleshipP4.hideturtle()

submarineP1 = t.Turtle()
submarineP1.hideturtle()
submarineP2 = t.Turtle()
submarineP2.hideturtle()
submarineP3 = t.Turtle()
submarineP3.hideturtle()

destroyerP1 = t.Turtle()
destroyerP1.hideturtle()
destroyerP2 = t.Turtle()
destroyerP2.hideturtle()
destroyerP3 = t.Turtle()
destroyerP3.hideturtle()

patrolBoatP1 = t.Turtle()
patrolBoatP1.hideturtle()
patrolBoatP2 = t.Turtle()
patrolBoatP2.hideturtle()

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
# The Turtles turn into Boats

def Carrier(wn):
    carrierP1.showturtle()
    carrierP1.penup()
    wn.addshape('BS--CarrierPart1.gif')
    carrierP1.shape('BS--CarrierPart1.gif')

    carrierP2.showturtle()
    carrierP2.penup()
    wn.addshape('BS--CarrierPart2.gif')
    carrierP2.shape('BS--CarrierPart2.gif')
        
    carrierP3.showturtle()
    carrierP3.penup()
    wn.addshape('BS--CarrierPart3.gif')
    carrierP3.shape('BS--CarrierPart3.gif')

    carrierP4.showturtle()
    carrierP4.penup()
    wn.addshape('BS--CarrierPart4.gif')
    carrierP4.shape('BS--CarrierPart4.gif')
    
    carrierP5.showturtle()
    carrierP5.penup()
    wn.addshape('BS--CarrierPart5.gif')
    carrierP5.shape('BS--CarrierPart5.gif')

def BattleShip(wn):
    battleshipP1.showturtle()
    battleshipP1.penup()
    wn.addshape('BS--BattleShipPart1.gif')
    battleshipP1.shape('BS--BattleShipPart1.gif')
    
    battleshipP2.showturtle()
    battleshipP2.penup()
    wn.addshape('BS--BattleShipPart2.gif')
    battleshipP2.shape('BS--BattleShipPart2.gif')
    
    battleshipP3.showturtle()
    battleshipP3.penup()
    wn.addshape('BS--BattleShipPart3.gif')
    battleshipP3.shape('BS--BattleShipPart3.gif')
     
    battleshipP4.showturtle()   
    battleshipP4.penup()
    wn.addshape('BS--BattleShipPart4.gif')
    battleshipP4.shape('BS--BattleShipPart4.gif')

def Submarine(wn):
    submarineP1.showturtle()
    submarineP1.penup()
    wn.addshape('BS--SubmarinePart1.gif')
    submarineP1.shape('BS--SubmarinePart1.gif')
    
    submarineP2.showturtle()
    submarineP2.penup()
    wn.addshape('BS--SubmarinePart2.gif')
    submarineP2.shape('BS--SubmarinePart2.gif')
    
    submarineP3.showturtle()
    submarineP3.penup()
    wn.addshape('BS--SubmarinePart3.gif')
    submarineP3.shape('BS--SubmarinePart3.gif')

def Destroyer(wn):
    destroyerP1.showturtle()
    destroyerP1.penup()
    wn.addshape('BS--DestroyerPart1.gif')
    destroyerP1.shape('BS--DestroyerPart1.gif')
    
    destroyerP2.showturtle()
    destroyerP2.penup()
    wn.addshape('BS--DestroyerPart2.gif')
    destroyerP2.shape('BS--DestroyerPart2.gif')
    
    destroyerP3.showturtle()
    destroyerP3.penup()
    wn.addshape('BS--DestroyerPart3.gif')
    destroyerP3.shape('BS--DestroyerPart3.gif')

def PatrolBoat(wn):
    patrolBoatP1.showturtle()
    patrolBoatP1.penup()
    wn.addshape('BS--PatrolBoatPart1.gif')
    patrolBoatP1.shape('BS--PatrolBoatPart1.gif')
    
    patrolBoatP2.showturtle()
    patrolBoatP2.penup()
    wn.addshape('BS--PatrolBoatPart2.gif')
    patrolBoatP2.shape('BS--PatrolBoatPart2.gif')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
# The Dragging of the Boats
   
def tugBoat(wn):
    def fxn1(carrierx, carriery):
        carrierP1.ondrag(None)
        carrierP2.ondrag(None)
        carrierP3.ondrag(None)
        carrierP4.ondrag(None)
        carrierP5.ondrag(None) 
        carrierP1.setheading(carrierP1.towards(carrierx, carriery))
        carrierP1.goto(carrierx, carriery)
        carrierP2.setheading(carrierP2.towards(carrierx, carriery))
        carrierP2.goto(carrierx, carriery - 88)
        carrierP3.setheading(carrierP3.towards(carrierx, carriery))
        carrierP3.goto(carrierx, carriery - 176)
        carrierP4.setheading(carrierP4.towards(carrierx, carriery))
        carrierP4.goto(carrierx, carriery - 264)
        carrierP5.setheading(carrierP5.towards(carrierx, carriery))
        carrierP5.goto(carrierx, carriery - 352)
        carrierP1.ondrag(fxn1)
        carrierP2.ondrag(fxn1)
        carrierP3.ondrag(fxn1)
        carrierP4.ondrag(fxn1)
        carrierP5.ondrag(fxn1)
    carrierP1.ondrag(fxn1)
    carrierP2.ondrag(fxn1)
    carrierP3.ondrag(fxn1)
    carrierP4.ondrag(fxn1)
    carrierP5.ondrag(fxn1)
    
    def fxn2(battleShipx, battleShipy):
        battleshipP1.ondrag(None)
        battleshipP2.ondrag(None)
        battleshipP3.ondrag(None)
        battleshipP4.ondrag(None) 
        battleshipP1.setheading(battleshipP1.towards(battleShipx, battleShipy))
        battleshipP1.goto(battleShipx, battleShipy)
        battleshipP2.setheading(battleshipP2.towards(battleShipx, battleShipy))
        battleshipP2.goto(battleShipx, battleShipy - 88)
        battleshipP3.setheading(battleshipP3.towards(battleShipx, battleShipy))
        battleshipP3.goto(battleShipx, battleShipy - 176)
        battleshipP4.setheading(battleshipP4.towards(battleShipx, battleShipy))
        battleshipP4.goto(battleShipx, battleShipy - 264)
        battleshipP1.ondrag(fxn2)
        battleshipP2.ondrag(fxn2)
        battleshipP3.ondrag(fxn2)
        battleshipP4.ondrag(fxn2)
    battleshipP1.ondrag(fxn2)
    battleshipP2.ondrag(fxn2)
    battleshipP3.ondrag(fxn2)
    battleshipP4.ondrag(fxn2)
    
    def fxn3(submarinex, submariney):
        submarineP1.ondrag(None)
        submarineP2.ondrag(None)
        submarineP3.ondrag(None) 
        submarineP1.setheading(submarineP1.towards(submarinex, submariney))
        submarineP1.goto(submarinex, submariney)
        submarineP2.setheading(submarineP2.towards(submarinex, submariney))
        submarineP2.goto(submarinex, submariney - 88)
        submarineP3.setheading(submarineP3.towards(submarinex, submariney))
        submarineP3.goto(submarinex, submariney - 176)
        submarineP1.ondrag(fxn3)
        submarineP2.ondrag(fxn3)
        submarineP3.ondrag(fxn3)
    submarineP1.ondrag(fxn3)
    submarineP2.ondrag(fxn3)
    submarineP3.ondrag(fxn3)
    
    def fxn4(destroyerx, destroyery):
        destroyerP1.ondrag(None)
        destroyerP2.ondrag(None)
        destroyerP3.ondrag(None) 
        destroyerP1.setheading(destroyerP1.towards(destroyerx, destroyery))
        destroyerP1.goto(destroyerx, destroyery)
        destroyerP2.setheading(destroyerP2.towards(destroyerx, destroyery))
        destroyerP2.goto(destroyerx, destroyery - 88)
        destroyerP3.setheading(destroyerP3.towards(destroyerx, destroyery))
        destroyerP3.goto(destroyerx, destroyery - 176)
        destroyerP1.ondrag(fxn4)
        destroyerP2.ondrag(fxn4)
        destroyerP3.ondrag(fxn4)
    destroyerP1.ondrag(fxn4)
    destroyerP2.ondrag(fxn4)
    destroyerP3.ondrag(fxn4)
    
    def fxn5(patrolx, patroly):
        patrolBoatP1.ondrag(None)
        patrolBoatP2.ondrag(None) 
        patrolBoatP1.setheading(patrolBoatP1.towards(patrolx, patroly))
        patrolBoatP1.goto(patrolx, patroly)
        patrolBoatP2.setheading(patrolBoatP2.towards(patrolx, patroly))
        patrolBoatP2.goto(patrolx, patroly - 88)
        patrolBoatP1.ondrag(fxn5)
        patrolBoatP2.ondrag(fxn5)
    patrolBoatP1.ondrag(fxn5)
    patrolBoatP2.ondrag(fxn5)
