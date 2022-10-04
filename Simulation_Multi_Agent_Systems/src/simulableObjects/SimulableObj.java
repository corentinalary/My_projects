package simulableObjects;

import gui.GUISimulator;

/**
 * Abstract class representing an object that can be simulated.
 *
 */
abstract public class SimulableObj {

	/**
	 * Abstract method to update the object with its new attributes whenever it is simulated
	 */
	abstract public void update();
	
	/**
	 * Abstract method rendering the object on the Specified GUISimulator
	 * 
	 * @param gui is the GUISimulator in which we want to add the object
	 */
	abstract public void render(GUISimulator gui);
}
