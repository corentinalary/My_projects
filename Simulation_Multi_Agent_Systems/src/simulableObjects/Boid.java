package simulableObjects;

import java.awt.Color;
import java.awt.geom.Point2D;
import gui.GUISimulator;
import gui.Oval;

/**
 * Class child from Ball implementing the Boid.
 *
 */
public class Boid extends Ball {
	
	public Point2D.Double acceleration; // Force applied on the boid
	static private double MIN_DIST=50; // Minimal distance two boids try to respect between each other
	static private double MAX_VELOCITY=10; // Maximal velocity of a boid
	static private double MIN_VELOCITY=5; // Minimal velocity of a boid
	static private double MAX_ACCELERATION=5; // The maximal force that can be appled on a boid
	static private double SIGHT_RANGE=200;
	static private double SIGHT_ANGLE = Math.PI;

	/**
	 * Constructor of the Boid object.
	 * The Boid is here seen as circle with special attributes. 
	 * 
	 * @param coo is the coordinates of the Boid
	 * @param speed is the speed vector of the Boid
	 * @param accel is the force vector applied on the Boid 
	 * @param radius is the radius of the circle representing the Boid
	 * @param color is the color of the Boid
	 */
	public Boid(Point2D.Double coo, Point2D.Double speed, Point2D.Double accel, int radius, Color color) {
		super(coo, speed, radius, color);
		this.acceleration = accel;
	}
	
	/**
	 * Constructor of the Boid object.
	 * 
	 * @param boid is the Boid object that we want to create
	 */
	public Boid(Boid boid) {
		super(boid.coo, boid.velocity, boid.radius, boid.color);
		this.acceleration = new Point2D.Double(boid.acceleration.x, boid.acceleration.y);
	}
	
	/**
	 * Method update the position of the Boid
	 */
	@Override
	public void update() {
		Boid.normalize(this.acceleration, 0, Boid.MAX_ACCELERATION);
		this.velocity.x += this.acceleration.x;
		this.velocity.y += this.acceleration.y;
		
		Boid.normalize(this.velocity, Boid.MAX_VELOCITY, Boid.MIN_VELOCITY);
		this.coo.x += this.velocity.x;
		this.coo.y += this.velocity.y;
	}
	
	/**
	 * Method updating the position of the Boid by taking into account the Borders
	 * 
	 * @param x_max is the x coordinate of the border not to cross
	 * @param y_max is the y coordinate of the border not to cross
	 */
	 @Override
	public void update(int x_max, int y_max) {

		if(this.coo.x < this.radius) {
				this.coo.x = x_max-this.radius;
		}
		if(this.coo.x > x_max - this.radius) {
			this.coo.x = this.radius;
		}
		if(this.coo.y < this.radius) {
			this.coo.y = y_max - this.radius;
		}
		if(this.coo.y > y_max - this.radius) {
			this.coo.y = this.radius;
		}
		 
		this.update();
	}
	
	@Override
	public String toString() {
		return "Boid[Coo:(" + this.coo.x + ", " + this.coo.y + ")" +
				"||Velocity:(" + this.velocity.x + ", " + this.velocity.y + ")" +
				"||Acceleration:(" + this.acceleration.x + ", " + this.acceleration.y + ")" +
				"||Radius:" + this.radius + "|Color:" + this.color.toString() + "]";
	}
	
	/**
	 * Method calculating the distance between a specified Boid and our current Boid.
	 * 
	 * @param boid is the Boid for which we want to calculate the distance to our current Boid.
	 * 
	 * @return the distance of the specified Boid to our current Boid
	 */
	public double distanceTo(Boid boid) {
		return Boid.norm(new Point2D.Double(this.coo.x - boid.coo.x, this.coo.y - boid.coo.y));
	}
	
	/**
	 * Method calculating if our current Boid sees the specified Boid.
	 * 
	 * @param boid is the Boid for which we want to know if he is seen or not by our current
	 * 
	 * @return is the boolean worthing true if our current Boid is able to see the specified Boid.
	 */
	public boolean sees(Boid boid) {
		// If the given boid is in range :
		if(this.distanceTo(boid) <= Boid.SIGHT_RANGE) {
			
			/* Calculating the angle between the direction of the current boid and the evaluated boid within range */
			Point2D.Double a = this.velocity; // Velocity vector, giving the direction of the current boid
			Point2D.Double b = new Point2D.Double(boid.coo.x - this.coo.x , boid.coo.y - this.coo.y ); // Vector from the current boid to the evaluated boid
			
			double alpha = Boid.getAngle(a);
			double beta = Boid.getAngle(b);
			
			double theta = alpha - beta;
			
			/* The boid doesn't see its neighbors if they are behind it, with an arbitrary angle */
			if (Math.abs(theta) <= Boid.SIGHT_ANGLE / 2) {
				return true;
			}
		}
		return false;
	}
	
	/**
	 * Getter
	 * 
	 * @return the x coordinate of the boid
	 */
	public double getXPos() {
		return this.coo.x;
	}
	/**
	 * Getter
	 * 
	 * @return the y coordinate of the boid
	 */
	public double getYPos() {
		return this.coo.y;
	}
	
	/**
	 * Getter
	 * 
	 * @return the x velocity of the boid
	 */
	public double getXVelocity() {
		return this.velocity.x;
	}
	/**
	 * Getter
	 * 
	 * @return the y velocity of the boid
	 */
	public double getYVelocity() {
		return this.velocity.y;
	}
	
	/**
	 * Method calculating the norm of a specified vector.
	 * 
	 * @param vect is the vector for which we want to calculate the norm
	 * 
	 * @return is the value of the norm of the specified vector
	 */
	static private double norm(Point2D.Double vect) {
		return Math.sqrt(Math.pow(vect.x, 2) + Math.pow(vect.y, 2));
	}
	
	/**
	 * Method calculating the angle between the specified vector and the 
	 * horizontal vector.
	 * 
	 * @param vect is the vector for which we want to calculate the angle
	 * 
	 * @return is the value of the angle expressed in radians.
	 */
	static private double getAngle(Point2D.Double vect) {
		if(vect.x == 0) { 
			if(vect.y >= 0) { return Math.PI/2; }
			return -Math.PI/2;
		}
		if(vect.y > 0) { return Math.acos(vect.x/norm(vect)); }
		return -Math.acos(vect.x/norm(vect));
	}
	
	/**
	 * Method normalizing a vector to a specified constant.
	 * 
	 * @param vect is the vector to normalize
	 * @param constant_max is the maximal value of the vector norm
	 * @param constant_min is the minimal value of the vector norm
	 */
	static public void normalize(Point2D.Double vect, double constant_min, double constant_max) {
		double alpha = getAngle(vect);
		
		if(Boid.norm(vect) > constant_max) {
			vect.x = (Math.cos(alpha) * constant_max);
			vect.y = (Math.sin(alpha) * constant_max);
		} else {
			if(Boid.norm(vect) < constant_min) {
				vect.x = (Math.cos(alpha) * constant_min);
				vect.y = (Math.sin(alpha) * constant_min);
			}
		}
	}
	
	/**
	 * Getter
	 * 
	 * @return the attribute MIN_VELOCITY
	 */
	static public double getMinVelocity() {
		return Boid.MIN_VELOCITY;
	}
	
	/**
	 * Getter
	 * 
	 * @return the attribute MAX_VELOCITY
	 */
	static public double getMaxVelocity() {
		return Boid.MAX_VELOCITY;
	}

	/**
	 * Getter
	 * 
	 * @return the attribute MIN_DIST
	 */
	static public double getMinDist() {
		return Boid.MIN_DIST;
	}
	
	/**
	 * Method rendering the boid on the specified GUISimulator.
	 * 
	 * @param gui is the GUISimulator on which the boid is rendered
	 */
	@Override
	public void render(GUISimulator gui) {
		super.render(gui);
		
		double alpha = Boid.getAngle(this.velocity);
		Point2D.Double direction = new Point2D.Double(Math.cos(alpha)*this.radius*0.375, Math.sin(alpha)*this.radius*0.375);
		
		gui.addGraphicalElement (new Oval((int) (this.coo.x + direction.x), (int) (this.coo.y + direction.y),
				Color.WHITE, Color.WHITE, Math.max(this.getRadius()/5, 1)));
	}
}
