package simulator;

import gui.GUISimulator;
import simulableObjSets.GridSchelling;
import event.GridEvent;

/**
 * Class child from Simulator implementing the simulator for a grid in the Schelling game.
 *
 */

public class GridSchellingSimulator extends Simulator {

	/**
	 * Constructor of the GridSchellingSimulator object
	 * 
	 * @param gui is the GUISimulator of the GridSchellingSimulator object
	 * @param size is the size of the grid within the GridSchellingSimulator object
	 * @param nbStates is the number of colors in the Schelling game
	 * @param K is the K parameter in the Schelling game
	 */
	public GridSchellingSimulator(GUISimulator gui, int size, int nbStates, int K) {
		super(gui, 1);
		this.objects[0] = new GridSchelling(size, nbStates, K);
		
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
