package simulableObjSets;

import java.awt.geom.Point2D;
import gui.GUISimulator;
import simulableObjects.Ball;

import java.awt.Color;

/**
 * Class representing the Balls object which is composed of several Ball objects.
 *
 */
public class Balls extends SimulableSets {
	
	private Ball[] balls; // Array with the current balls
	private Ball[] initBalls; // Array of the balls at their initial states
	private int ballsNumber;
	private int radius;
	private Color color;
	static private int x_max = 750;
	static private int y_max = 550;
	
	/**
	 * Constructor of the Balls objects.
	 * The "balls" attribute is a table of Ball objects composing Balls.
	 * The "initBalls" is a table of Ball objects composing Balls at his creation.
	 * 
	 * @param ballsNumber is the number of Ball objects composing Balls
	 * @param radius is the radius of the Ball objects composing Balls
	 * @param color is the color of the Ball objects composing Balls
	 */
	public Balls(int ballsNumber, int radius, Color color) {
		if(ballsNumber < 0) { throw new IllegalArgumentException("The number of balls cannot be negative ! "); }
		this.ballsNumber = ballsNumber;
		
		if(radius < 0) { throw new IllegalArgumentException("The ball radius cannot be negative ! "); }
		this.radius = radius;
		
		this.color = color;
		
		this.balls = new Ball[ballsNumber];
		this.initBalls = new Ball[ballsNumber];
		
		/* Randomly placing the balls and choosing their velocity, with arbitrary limits */
		for(int i = 0; i < this.ballsNumber; i++) {
			double cooX = Math.random() * Balls.x_max;
			double cooY = Math.random() * Balls.y_max;
			double velX = Math.random() * 10;
			double velY = Math.random() * 10;
			this.balls[i] = new Ball(new Point2D.Double(cooX, cooY), new Point2D.Double(velX, velY), this.radius, this.color);
			
			// Initialization of the initial states array
			this.initBalls[i] = new Ball(this.balls[i]);
		}
	}
	
	/**
	 * Method updating the coordinates of each Ball object composing Balls.
	 */
	public void update() {
		for(int i = 0; i < this.ballsNumber; i++) {
			this.balls[i].update();
		}
	}
	
	/**
	 * Method updating the coordinates of each Ball object composing Balls and 
	 * taking into account the borders.
	 * 
	 * @param x_max is the x coordinate of the border
	 * @param y_max is the y coordinate of the border
	 */
	public void update(int x_max, int y_max) {
		for(int i = 0; i < this.ballsNumber; i++) {
			this.balls[i].update(x_max, y_max);
		}
	}
	/**
	 * Method reinitializing each Ball object of Balls with its 
	 * initial value.
	 * 
	 */
	public void reInit(){
		for(int i = 0; i < this.ballsNumber; i++) {
			this.balls[i] = new Ball(this.initBalls[i]);
		}
	}
	
	/**
	 * 
	 * Method rendering all the Ball objects of Balls on the 
	 * GUISimulator gui.
	 * 
	 * @param gui is the GUISimulator on which to render all the Ball objects of Balls
	 */
	public void render(GUISimulator gui) {
		for(int i = 0; i < this.ballsNumber; i++) {
			this.balls[i].render(gui);
		}
	}
	
	@Override
	public String toString() {
		String ballsString="";
		for(int i = 0; i < this.ballsNumber; i++) {
			ballsString += this.balls[i].toString();
		}
		return ballsString;
	}

}
