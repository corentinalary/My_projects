package event;

import gui.GUISimulator;
import simulableObjSets.SimulableSets;

/**
 * Class implementing an Event
 *
 */
public class Event {
	
	protected SimulableSets obj;
	protected GUISimulator gui;
	public long date; // Date on which the event is supposed to be played
	
	/**
	 * Constructor of the Event object
	 * 
	 * @param date is the date of the event
	 * @param obj is the object concerned by the event
	 * @param gui is the GUISimulator showing the event
	 */
	public Event(long date, SimulableSets obj, GUISimulator gui ) {
		this.obj = obj;
		this.date = date;
		this.gui = gui;
	}
	
	/**
	 * Method executing the event
	 */
	public void execute() {
		this.obj.update();
	}
	
	/**
	 * Getter
	 * 
	 * @return the date attribute
	 */
	public long getDate() {
		return this.date;
	}
}