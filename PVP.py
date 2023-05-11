import turtle as t
import ShipYard as ship
import NavalWarfare as warGrid
import GFCS as gfcs

wn = t.Screen()

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
# The Timer Dictating the Placing of the Ships or the Usage of the Targeting System

timer = 3

def moreGameplay():
    global timer
    
    if timer >= 1:
        ship.tugBoat(wn) 
    if timer <= 0:
        gfcs.targeting(wn)
    
    timer = timer - 1
    wn.ontimer(moreGameplay,10000)
   
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Causes PVP to Run
 
def GamePlay():
    warGrid.gridMaker(wn)
    ship.Carrier(wn)
    ship.BattleShip(wn)
    ship.Submarine(wn)
    ship.Destroyer(wn)
    ship.PatrolBoat(wn)
    moreGameplay()
 