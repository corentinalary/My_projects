package event;

import java.util.LinkedList;

/**
 * Class implementing the event manager.
 *
 */
public class EventManager {
	
	LinkedList<Event> eventsToProcess;
	
	private long currentDate;
	
	/**
	 * Constructor of the EventManager object
	 */
	public EventManager() {
		this.currentDate = 0;
		this.eventsToProcess = new LinkedList< Event>();
	}
	
	/**
	 * Method adding an event to the EventManager.
	 * 
	 * @param e is the event to add
	 */
	public void addEvent(Event e) {
		this.eventsToProcess.add(e);
	}
	
	/**
	 * Method treating the events to the next date in the EventManager.
	 */
	public void next() {
		
		this.currentDate += 1;
		LinkedList<Event> toDelete = new LinkedList<Event>();
		
		for (Event e : this.eventsToProcess) {		
			if(e.date == this.currentDate) {
				e.execute();
				toDelete.add(e);
			}		
		}
		
		for (Event e : toDelete) {		
			this.eventsToProcess.remove(e);	
		}
	}
	
	/**
	 * Method return the state of the EventManager.
	 * 
	 * @return true if the EventManager has treated all the events and false otherwise.
	 */
	public boolean isFinished() {
		return this.getEventsToProcess().isEmpty();
	}
	
	/**
	 * Method reseting the date of the EventManager to 0 and thus restarting it.
	 */
	public void restart() {
		this.currentDate = 0;
		this.eventsToProcess.clear();
	}
	
	/**
	 * Getter
	 * 
	 * @return the eventsToProcess attribut.
	 */
	public LinkedList<Event> getEventsToProcess() {
		return eventsToProcess;
	}

	/**
	 * Setter
	 * 
	 * @param eventsToProcess is the new value of the eventsToProcess attribute.
	 */
	public void setEventsToProcess(LinkedList<Event> eventsToProcess) {
		this.eventsToProcess = eventsToProcess;
	}
	
	/**
	 * Getter
	 * 
	 * @return the currentDate attribute
	 */
	public long getCurrentDate() {
		return this.currentDate;
	}
}
