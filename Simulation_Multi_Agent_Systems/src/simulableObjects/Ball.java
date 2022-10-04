package simulableObjects;

import java.awt.Color;
import java.awt.geom.Point2D;
import gui.GUISimulator;
import gui.Oval;
/**
 * This class is a child from the class SimulableObj and represents a ball.
 * Here we see a ball as a circle with an origin and a radius.
 * 
 */
public class Ball extends SimulableObj {
	protected Point2D.Double coo;
	protected Point2D.Double velocity;
	protected int radius;
	protected Color color;
	
	/**
	 * Constructor of the ball object
	 * 
	 * @param coo are the x and y coordinates of the center of the circle representing the ball 
	 * @param velocity represents the velocity vector of the ball
	 * @param radius is the radius of the circle representing the ball
	 * @param color is the color of the ball
	 */
	public Ball(Point2D.Double coo, Point2D.Double velocity, int radius, Color color) {
		this.coo = new Point2D.Double(coo.x, coo.y);
		this.velocity = new Point2D.Double(velocity.x, velocity.y);
		
		if(radius <= 0) {throw new IllegalArgumentException("The given radius cannot be negative or null !"); }
		this.radius = radius;
		this.color = color;
	}
	/**
	 * Constructor by copy of the ball object
	 * 
	 * @param ball is the ball to copy
	 */
	public Ball(Ball ball) {
		this.coo = new Point2D.Double(ball.coo.x, ball.coo.y);
		this.velocity = new Point2D.Double(ball.velocity.x, ball.velocity.y);
		this.radius = ball.radius;
		this.color = ball.color;
	}
	/**
	 * Method updating the position of the ball by taking into account the speed of the ball
	 */
	public void update() {
		this.coo.x += this.velocity.x;
		this.coo.y += this.velocity.y;
	}
	/**
	 * 
	 * Method updating the position of the ball by taking into account the speed of the ball
	 * and by restricting the area in which the ball can move. The ball is able to "bounce"
	 * on the borders.
	 * 
	 * @param x_max is the limit of the ball in the x axis
	 * @param y_max is the limit of the ball in the y axis
	 */
	public void update(int x_max, int y_max) {
		this.update();
		
		/* Adjusting the coordinates and the speed if a border is met*/
		// Left border
		if(this.coo.x <= this.radius) {
			this.coo.x = this.radius;
			this.velocity.x = -this.velocity.x;
		}
		// Right border
		if(this.coo.x >= x_max-this.radius) {
			this.coo.x = x_max-this.radius;
			this.velocity.x = -this.velocity.x;
		}
		// Upper border
		if(this.coo.y <= this.radius) {
			this.coo.y = this.radius;
			this.velocity.y = -this.velocity.y;
		}
		// Lower border
		if(this.coo.y >= y_max-this.radius) {
			this.coo.y = y_max-this.radius;
			this.velocity.y = -this.velocity.y;
		}
	}
	/**
	 * Method changing the position of the ball with specified coordinates.
	 * 
	 * @param x is the new x coordinate of the ball
	 * @param y is the new y coordinate of the ball
	 */
	public void setPos(int x, int y) {
		this.coo.x = x;
		this.coo.y = y;
	}
	
	/**
	 * Getter
	 * 
	 * @return the radius of the ball
	 */
	public int getRadius() {
		return this.radius;
	}
	
	/**
	 * Method rendering the ball on the specified GUISimulator.
	 * 
	 * @param gui is the GUISimulator on which the ball is rendered
	 */
	public void render(GUISimulator gui) {
		gui.addGraphicalElement (new Oval((int) this.coo.x, (int) this.coo.y,
				this.color, this.color, this.radius));
	}
	
	@Override
	public String toString() {
		return "Ball[Coo:(" + this.coo.x + ", " + this.coo.y + ")" +
				"||Velocity:(" + this.velocity.x + ", " + this.velocity.y + ")" +
				"||Radius:" + this.radius + "|Color:" + this.color.toString() + "]";
	}
}
