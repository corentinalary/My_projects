package simulator;

import gui.GUISimulator;
import simulableObjSets.Grid;
import event.GridEvent;

/**
 * Class child from Simulator implementing the simulator for a grid.
 *
 */
public class GridSimulator extends Simulator {

	/**
	 * Constructor of the GridSimulator object
	 * 
	 * @param gui is the GUISimulator within the GridSimulator object
	 * @param size is the size of the grid within GridSimulator object
	 */
	public GridSimulator(GUISimulator gui, int size) {
		super(gui, 1);
		this.objects[0] = new Grid(size, 2);
		
		/* Adding the initial event, so that the grid is updated on date 0 */
		this.manager.addEvent(new GridEvent(0, this.objects[0], this.gui));
		
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
