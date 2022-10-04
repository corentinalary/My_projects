package simulator;

import gui.GUISimulator;
import simulableObjSets.GridImmigration;
import event.GridEvent;

/**
 * Class child from Simulator implementing the Simulator for the grid of the immigration game.
 *
 */
public class GridImmigrationSimulator extends Simulator {

	/**
	 * Constructor of the GridImmigrationSimulator
	 * 
	 * @param gui is the GUISimulator of the GridImmigrationSimulator object
	 * @param size is the size of the grid within the GridImmigrationSimulator object
	 * @param nbStates is the number of states in the cells within the grid composing the GridImmigrationSimulator object
	 */
	public GridImmigrationSimulator(GUISimulator gui, int size, int nbStates) {
		super(gui, 1);
		this.objects[0] = new GridImmigration(size, nbStates);
		
		this.render();
	}
	
	/**
	 * Method implementing the action when a user presses the next button.
	 */
	@Override
	public void next() {
		long date = this.manager.getCurrentDate();
		
		/* Adding the events for the grid to be updated on next date */
		this.manager.addEvent(new GridEvent(date+1, this.objects[0], this.gui));
		
		/* Playing all the events of the current date */
		this.manager.next();
		
		this.render();
	}
}
