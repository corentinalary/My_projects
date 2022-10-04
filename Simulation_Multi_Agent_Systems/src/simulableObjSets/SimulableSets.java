package simulableObjSets;

import gui.GUISimulator;
/**
 * Abstract class representing an object that can be simulated.
 *
 */
abstract public class SimulableSets {
	
	/**
	 * Abstract method to update the objects with their new attributes and by taking
	 *  into account the borders. By default, the boundary is not taken into account.
	 * 
	 * @param x_max is the x coordinate of the border
	 * @param y_max is the y coordinate of the border
	 * 
	 */
	public void update(int x_max, int y_max) {this.update();}
	
	/**
	 * Abstract method for updating the object with his new attributes whenever he is simulated
	 */
	abstract public void update();
	
	/**
	 * Abstract method reinitializing the SimulableObjects
	 */
	abstract public void reInit();
	
	/**
	 * Abstract method rendering the object on the Specified GUISimulator 
	 * 
	 * @param gui is the GUISimulator in which we want to add the object
	 */
	abstract public void render(GUISimulator gui);
}
