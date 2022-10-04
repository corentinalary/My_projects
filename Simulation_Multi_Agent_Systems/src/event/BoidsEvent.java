package event;

import gui.GUISimulator;
import simulableObjSets.SimulableSets;

/**
 * Class child of Event representing an event on a specified Boids object
 * 
 */
public class BoidsEvent extends Event {

	/**
	 * Constructor of the BoidsEvent object.
	 * 
	 * @param date is the date of the BoidsEvent
	 * @param obj is the Boids object composing the BoidsEvent
	 * @param gui is the GUISimulator associated with the BoidsEvent
	 */
	public BoidsEvent(long date, SimulableSets obj, GUISimulator gui ) {	
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
