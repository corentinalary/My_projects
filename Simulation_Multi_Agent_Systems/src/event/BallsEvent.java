package event;

import gui.GUISimulator;
import simulableObjSets.SimulableSets;

/**
 * Class child from Event representing an event on a Balls object.
 *
 */
public class BallsEvent extends Event {
	
	/**
	 * Constructor of a BallsEvent object.
	 * 
	 * @param date is the date of the event on the Balls object
	 * @param obj is the Balls object on which the event happen
	 * @param gui is the GUISimulator showing what the event on the Balls object is.
	 */
	public BallsEvent(long date, SimulableSets obj, GUISimulator gui ) {
		super(date, obj, gui);
	}

	/**
	 * Method executing the event
	 */
	@Override
	public void execute() {
		this.obj.update(this.gui.getPanelWidth(), this.gui.getPanelHeight());
	}
}
