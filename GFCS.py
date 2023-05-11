import turtle as t
from turtle import *
import ShipYard as ship

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
# The Targeting Stystem

def targeting(wn):
    bombingArea = t.Turtle()
    bombingArea.penup()
    wn.addshape('Aim1.gif')
    wn.addshape('EXPLOSION.gif')
    collisionDistance = 50
    
    bombingArea.shape('Aim1.gif')
    
    # ---------------------------------------------------------------------------------------------------------------------------------------------------------------
    # The Inputs for X and Y Cordinates on Where to Fire
    
    targetx = numinput("Target System x", "Where are You Shooting (x)")
    targety = numinput("Target System y", "Where are You Shooting (y)")

    bombingArea.goto(targetx, targety)
    
    # ---------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Checks For Hits
    
    def carrierHit():
        if (abs(bombingArea.xcor() - ship.carrierP1.xcor()) < collisionDistance):
            if (abs(bombingArea.ycor() - ship.carrierP1.ycor()) < collisionDistance):
                bombingArea.shape('EXPLOSION.gif')
                bombingArea.stamp()

        if (abs(bombingArea.xcor() - ship.carrierP2.xcor()) < collisionDistance):
            if (abs(bombingArea.ycor() - ship.carrierP2.ycor()) < collisionDistance):
                bombingArea.shape('EXPLOSION.gif')
                bombingArea.stamp()

        if (abs(bombingArea.xcor() - ship.carrierP3.xcor()) < collisionDistance):
            if (abs(bombingArea.ycor() - ship.carrierP3.ycor()) < collisionDistance):
                bombingArea.shape('EXPLOSION.gif')
                bombingArea.stamp()

        if (abs(bombingArea.xcor() - ship.carrierP4.xcor()) < collisionDistance):
            if (abs(bombingArea.ycor() - ship.carrierP4.ycor()) < collisionDistance):
                bombingArea.shape('EXPLOSION.gif')
                bombingArea.stamp()

        if (abs(bombingArea.xcor() - ship.carrierP5.xcor()) < collisionDistance):
            if (abs(bombingArea.ycor() - ship.carrierP5.ycor()) < collisionDistance):
                bombingArea.shape('EXPLOSION.gif')
                bombingArea.stamp()
    
    def battleshipHit():
        if (abs(bombingArea.xcor() - ship.battleshipP1.xcor()) < collisionDistance):
            if (abs(bombingArea.ycor() - ship.battleshipP1.ycor()) < collisionDistance):
                bombingArea.shape('EXPLOSION.gif')
                bombingArea.stamp()
        
        if (abs(bombingArea.xcor() - ship.battleshipP2.xcor()) < collisionDistance):
            if (abs(bombingArea.ycor() - ship.battleshipP2.ycor()) < collisionDistance):
                bombingArea.shape('EXPLOSION.gif')
                bombingArea.stamp()
        
        if (abs(bombingArea.xcor() - ship.battleshipP3.xcor()) < collisionDistance):
            if (abs(bombingArea.ycor() - ship.battleshipP3.ycor()) < collisionDistance):
                bombingArea.shape('EXPLOSION.gif')
                bombingArea.stamp()
        
        if (abs(bombingArea.xcor() - ship.battleshipP4.xcor()) < collisionDistance):
            if (abs(bombingArea.ycor() - ship.battleshipP4.ycor()) < collisionDistance):
                bombingArea.shape('EXPLOSION.gif')
                bombingArea.stamp()
                
    def submarineHit():
        if (abs(bombingArea.xcor() - ship.submarineP1.xcor()) < collisionDistance):
            if (abs(bombingArea.ycor() - ship.submarineP1.ycor()) < collisionDistance):
                bombingArea.shape('EXPLOSION.gif')
                bombingArea.stamp()
        
        if (abs(bombingArea.xcor() - ship.submarineP2.xcor()) < collisionDistance):
            if (abs(bombingArea.ycor() - ship.submarineP2.ycor()) < collisionDistance):
                bombingArea.shape('EXPLOSION.gif')
                bombingArea.stamp()
        
        if (abs(bombingArea.xcor() - ship.submarineP3.xcor()) < collisionDistance):
            if (abs(bombingArea.ycor() - ship.submarineP3.ycor()) < collisionDistance):
                bombingArea.shape('EXPLOSION.gif')
                bombingArea.stamp()
    
    def destroyerHit():
        if (abs(bombingArea.xcor() - ship.destroyerP1.xcor()) < collisionDistance):
            if (abs(bombingArea.ycor() - ship.destroyerP1.ycor()) < collisionDistance):
                bombingArea.shape('EXPLOSION.gif')
                bombingArea.stamp()
        
        if (abs(bombingArea.xcor() - ship.destroyerP2.xcor()) < collisionDistance):
            if (abs(bombingArea.ycor() - ship.destroyerP2.ycor()) < collisionDistance):
                bombingArea.shape('EXPLOSION.gif')
                bombingArea.stamp()
        
        if (abs(bombingArea.xcor() - ship.destroyerP3.xcor()) < collisionDistance):
            if (abs(bombingArea.ycor() - ship.destroyerP3.ycor()) < collisionDistance):
                bombingArea.shape('EXPLOSION.gif')
                bombingArea.stamp()
        
    def patrolboatHit():
        if (abs(bombingArea.xcor() - ship.patrolBoatP1.xcor()) < collisionDistance):
            if (abs(bombingArea.ycor() - ship.patrolBoatP1.ycor()) < collisionDistance):
                bombingArea.shape('EXPLOSION.gif')
                bombingArea.stamp()
        
        if (abs(bombingArea.xcor() - ship.patrolBoatP2.xcor()) < collisionDistance):
            if (abs(bombingArea.ycor() - ship.patrolBoatP2.ycor()) < collisionDistance):
                bombingArea.shape('EXPLOSION.gif')
                bombingArea.stamp()
                
    def checkHit():
        carrierHit()
        battleshipHit()
        submarineHit()
        destroyerHit()
        patrolboatHit()
 
    checkHit()
    