package simulator;

import java.awt.Color;
import gui.GUISimulator;
import simulableObjSets.Boids;
import event.BoidsEvent;

/**
 * Class child from Simulator implementing the simulator of Boids
 *
 */
public class BoidsSimulator extends Simulator {
	
	/**
	 * Constructor for the BoidsSimulator object
	 * 
	 * @param gui is the GUISimulator associated with the BoidsSimulator
	 */
	public BoidsSimulator(GUISimulator gui) {
		super(gui, 2);
		this.objects[0] = new Boids(10, gui.getPanelWidth(), gui.getPanelHeight(), 15, Color.RED); // 10 red boids of radius 15
		this.objects[1] = new Boids(20, gui.getPanelWidth(), gui.getPanelHeight(), 10, Color.GREEN); // 20 green boids of radius 10
		
		/* Adding initial events, so that each group is updated on date 0 */
		this.manager.addEvent(new BoidsEvent(0, this.objects[0], this.gui));
		this.manager.addEvent(new BoidsEvent(0, this.objects[1], this.gui));
		
		this.render();
	}
	
	/**
	 * Method implementing the action whenever a user presses the button next
	 */
	@Override
	public void next() {
		long date = this.manager.getCurrentDate();
		
		/* Adding the events for the balls to be updated on next date */
		this.manager.addEvent(new BoidsEvent(date+1, this.objects[0], this.gui));
		if(date %2 == 0) {
			// The second group of boids is 2 times less reactive than the first one
			this.manager.addEvent(new BoidsEvent(date+1, this.objects[1], this.gui));
		}
		
		/* Playing all the events of the current date */
		this.manager.next();
		
		this.render();
	}
}
