package simulableObjSets;


import java.awt.geom.Point2D;
import java.awt.Color;
import gui.GUISimulator;
import simulableObjects.Boid;

/**
 * Class child from SimulableObjects representing a group of Boid.
 *
 */

public class Boids extends SimulableSets {
	
	private Boid[] boids;
	private Boid[] initBoids;
	private int size;
	private int radius;
	private Color color;
	
	/**
	 * Constructor of the Boids object
	 * 
	 * @param size is the number of Boid objects composing Boids
	 * @param x_max is the x coordinate of the border not to cross
	 * @param y_max is the y coordinate of the border not to cross
	 * @param radius is the radius of the Boid objects composing Boids
	 * @param color is the color of the Boid objects composing Boids
	 */
	public Boids(int size, int x_max, int y_max, int radius, Color color) {
		if(size < 0) { throw new IllegalArgumentException("The number of boids cannot be negative !"); }
		this.size = size;
		
		if(x_max < 0) { throw new IllegalArgumentException("Maximal x boundary cannot be negative !"); }
		if(y_max < 0) { throw new IllegalArgumentException("Maximal y boundary cannot be negative !"); }
		
		this.radius = radius;
			
		this.boids = new Boid[this.size];
		this.initBoids = new Boid[this.size];
		
		this.color = color;
		
		for(int i = 0; i < this.size; i++) {
			double posX = Math.random() * x_max;
			double posY = Math.random() * y_max;
			Point2D.Double coo = new Point2D.Double(posX, posY);
			
			double velX = Math.random() * (2*Boid.getMaxVelocity()) - Boid.getMaxVelocity();
			double velY = Math.random() * (2*Boid.getMaxVelocity()) - Boid.getMaxVelocity();
			Point2D.Double speed = new Point2D.Double(velX, velY);
			Boid.normalize(speed, Boid.getMinVelocity(), Boid.getMaxVelocity());
			
			Point2D.Double accel = new Point2D.Double(0, 0);
			this.boids[i] = new Boid(coo, speed, accel, this.radius, this.color);
			this.initBoids[i] = new Boid(this.boids[i]);
		}
	}
	
	/**
	 * Method calculating the acceleration of the specified Boid object in Boids
	 * 
	 * @param i is number of the Boid in Boids for which we want to calculate the acceleration
	 *  
	 * @return the acceleration of the specified Boid
	 */
	private Point2D.Double acceleration(int i) {
		Point2D.Double target = new Point2D.Double(this.boids[i].getXPos(), this.boids[i].getYPos());
		Point2D.Double acceleration = new Point2D.Double(0, 0);
		
		double S_x = 0;
		double S_y = 0;
		int count = 0;
		
		for(int j = 0; j < this.size; j++) { 
			if(j != i && this.boids[i].sees(this.boids[j]))
			{
				if(this.boids[i].distanceTo((this.boids[j])) >= Boid.getMinDist()) {
					S_x += this.boids[j].getXPos();
					S_y += this.boids[j].getYPos();
				}
				else {
					S_x += (2*this.boids[i].getXPos() - this.boids[j].getXPos());
					S_y += (2*this.boids[i].getXPos() - this.boids[j].getXPos());
				}
				count++;
			}
		}
		
		// If the boid doesn't see any neighbor, it continues on its way
		if(count == 0) { return acceleration; }
		
		target.x = S_x/count;
		target.y = S_y/count;
		
		Point2D.Double desired_velocity = new Point2D.Double(target.x - this.boids[i].getXPos(), target.y - this.boids[i].getYPos());
		Boid.normalize(desired_velocity, Boid.getMinVelocity(), Boid.getMaxVelocity());

		acceleration.x = desired_velocity.x - this.boids[i].getXVelocity();
		acceleration.y = desired_velocity.y - this.boids[i].getYVelocity();
		
		return acceleration;
	}

	/**
	 * Method updating the position of the Boid objects composing Boids
	 */
	public void update() {
		for(int i = 0; i < this.size; i++) {
			Point2D.Double new_force = acceleration(i);
			this.boids[i].acceleration.x += new_force.x;
			this.boids[i].acceleration.y += new_force.y;
		}
		
		for(int i = 0; i < this.size; i++) {
			this.boids[i].update();
		}
	}
	
	/**
	 * Method updating the position of the Boid objects composing Boids by taking into account the borders.
	 * 
	 * @param x_max coordinate of the border not to cross
	 * @param y_max coordinate of the border not to cross
	 * 
	 */
	public void update(int x_max, int y_max) {
		
		for(int i = 0; i < this.size; i++) {
			this.boids[i].acceleration = acceleration(i);
		}
		
		for(int i = 0; i < this.size; i++) {
			this.boids[i].update(x_max, y_max);
		}
	}
	
	/**
	 * Method reinitializing the Boid objects composing Boids.
	 */
	public void reInit() {
		this.boids = new Boid[this.size];
		
		for(int i = 0; i < this.size; i++) {
			this.boids[i] = new Boid(this.initBoids[i]);
		}
	}
	
	
	/**
	 * Method adding the Boid objects composing Boids on the specified GUISimulator
	 * 
	 * @param gui is the GUISimator in which we want to add Boids 
	 */
	public void render(GUISimulator gui) {
		for(int i = 0; i < this.size; i++) { this.boids[i].render(gui); }
	}
	
	/**
	 * Method printing the values of the Boid objects in Boids
	 */
	public void print() {
		System.out.println("Printing current Boids : ");
		for(int i = 0; i < this.size; i++) {
			System.out.println(this.boids[i].toString());
		}
	}
}
