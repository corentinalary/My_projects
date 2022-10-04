package simulator;

import gui.GUISimulator;
import gui.Simulable;
import simulableObjSets.SimulableSets;
import event.EventManager;
import event.Event;

/**
 * Class representing a simulator which is the element that makes the link 
 * between the object, the EventManager and the GUISimulator during the simulation.
 *
 */

public class Simulator implements Simulable {
	
	protected GUISimulator gui;
	protected EventManager manager;
	protected SimulableSets[] objects;
	protected int nbSets;
	
	/**
	 * Constructor of the Simulator object.
	 * 
	 * @param gui is the GUISimulator within the Simulator object
	 * @param nbSets is the number of different sets of simulable objects
	 */
	public Simulator(GUISimulator gui, int nbSets) {
		this.gui = gui;
		this.manager = new EventManager();
		
		if(nbSets < 0) { throw new IllegalArgumentException("The number of different sets cannot be negative"); }
		this.nbSets = nbSets;
		
		this.objects = new SimulableSets[this.nbSets];
	}
	
	/**
	 * Method implementing the action when the user presses the next button.
	 */
	public void next() {
		long date = this.manager.getCurrentDate();
		
		for(int i = 0; i < this.nbSets; i++) {
			this.manager.addEvent(new Event(date+1, this.objects[i], this.gui));
		}
		this.render();
	}
	
	/**
	 * Method restarting the simulation
	 */
	public void restart() {
		System.out.println("Restarting...");
		
		for(int i = 0; i < this.nbSets; i++) {
			this.objects[i].reInit();	
		}
		this.render();
	}
	
	/**
	 * Method updating the state of the objects in the GUISimulator of the Simulator object
	 */
	public void render() {
		this.gui.reset();
		for(int i = 0; i < this.nbSets; i++) {
			this.objects[i].render(this.gui);	
		}
	}
}
