package simulator;

import java.awt.Color;
import gui.GUISimulator;
import simulableObjSets.Balls;
import event.BallsEvent;

/**
 * Class child from Simulator representing the simulator of a Balls object.
 *
 */
public class BallsSimulator extends Simulator {
	
	/**
	 * Constructor of the BallsSimulator object 
	 * which make the link between Balls objects and 
	 * a GUISimulator showing the current state of the Balls objects.
	 * 
	 * @param gui is the GUISimulator showing the state of the Balls objects associated with the BallsSimulator
	 */
	public BallsSimulator(GUISimulator gui) {
		super(gui, 2);
		this.objects[0] = new Balls(3, 40, Color.RED); // 3 red balls of radius 40
		this.objects[1] = new Balls(2, 30, Color.GREEN); // 2 green balls of radius 30
		
		/* Adding initial events, so that each group is updated on date 0 */
		this.manager.addEvent(new BallsEvent(0, this.objects[0], this.gui));
		this.manager.addEvent(new BallsEvent(0, this.objects[1], this.gui));
		
		this.render();
	}
	
	/**
	 * Method implementing the evolution of the simulation
	 * when the user press the next button
	 */
	@Override
	public void next() {
		long date = this.manager.getCurrentDate();
		
		/* Adding the events for the balls to be updated on next date */
		this.manager.addEvent(new BallsEvent(date+1, this.objects[0], this.gui));
		this.manager.addEvent(new BallsEvent(date+1, this.objects[1], this.gui));
		
		/* Playing all the events of the current date */
		this.manager.next();
		
		this.render();
	}
}
