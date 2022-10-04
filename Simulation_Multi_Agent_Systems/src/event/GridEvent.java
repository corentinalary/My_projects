package event;

import gui.GUISimulator;
import simulableObjSets.SimulableSets;

/**
 * Class child of Event implementing an event on the grid
 * 
 */

public class GridEvent extends Event {
	
	/**
	 * Constructor of the GridEvent object
	 * 
	 * @param date is the date of the event
	 * @param obj is the Grid object of the event
	 * @param gui is the GUISimulator of the event
	 */
	public GridEvent(long date, SimulableSets obj, GUISimulator gui) {	
		super(date, obj, gui);
	}
}

