package simulableObjSets;

import simulableObjects.Cell;

/**
 * Class child of Grid implementing the grid for the immigration game.
 *
 */

public class GridImmigration extends Grid {

	/**
	 * Constructor of the GridImmigration object
	 * 
	 * @param size is the size of the grid
	 * @param nbStates is the number of the states of the cells within the grid
	 */
	public GridImmigration(int size, int nbStates) {
		super(size, nbStates);
	}
	
	/**
	 * Method updating the grid with the rules of the Immigration game
	 */
	@Override
	public void update() {
		for(int i = 0; i < this.gridSize; i++) {
			for(int j = 0; j < this.gridSize; j++) {
				int neighbors = this.getNbneighbors(this.grid[i][j]);
				
				// If there are enough neighbors of a given color, proceed to the next state on next iteration
				if(neighbors >= 3) {
					this.grid[i][j].setNextCellType((this.grid[i][j].getCellType() + 1) % this.nbStates);
				}
			}
		}
		
		/* Updating each cell */
		for(int i = 0; i < this.gridSize; i++) {
			for(int j = 0; j < this.gridSize; j++) {
				this.grid[i][j].update();
			}
		}
	}
	
	/**
	 * Method checking for a specified cell and a specified neighbor if the neighbor is in the next state 
	 * compared to the current cell
	 * 
	 * @param currentCell is the cell to study
	 * @param neighbor is the neighbor to study
	 * 
	 * @return true if the neighbor is in the next state, else false
	 */
	@Override
	protected boolean isNeighbor(Cell currentCell, Cell neighbor) {
		if(neighbor.getCellType() == ((currentCell.getCellType() + 1) % this.nbStates)) { return true; }
		return false;
	}
	
}