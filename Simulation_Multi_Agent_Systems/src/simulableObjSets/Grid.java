package simulableObjSets;

import java.awt.Point;
import gui.GUISimulator;
import simulableObjects.Cell;

/**
 * Class child from SimulableObjects implementing the Grid.
 *
 */
public class Grid extends SimulableSets {
	
	protected Cell grid[][];
	protected Cell initGrid[][];
	protected int gridSize;
	protected int nbStates;
	
	/**
	 * Constructor of the Grid object
	 * 
	 * @param size is the size of the grid
	 * @param nbStates is the number of the states in the cells composing the Grid
	 */
	public Grid(int size, int nbStates) {
		if(nbStates < 0) { throw new IllegalArgumentException("The number of different states cannot be negative"); }
		this.nbStates = nbStates;
		
		if(size <= 0) { throw new IllegalArgumentException("The grid size cannot be negative or null"); }
		
		this.gridSize = size;
		this.grid = new Cell[this.gridSize][this.gridSize];
		this.initGrid = new Cell[this.gridSize][this.gridSize];
		
		/* Initializing the grid with random values */
		for(int i = 0; i < this.gridSize; i++) {
			for(int j = 0; j < this.gridSize; j++) {
				double state = Math.random()*nbStates;
				
				this.grid[i][j] = new Cell(new Point(i, j), (int) state);
				this.initGrid[i][j] =  new Cell(this.grid[i][j]);
			}
		}
	}
	
	/**
	 * Method updating the cells of the Grid with the rules of Conway 
	 */
	public void update() {
		for(int i = 0; i < this.gridSize; i++) {
			for(int j = 0; j < this.gridSize; j++) {
				
				// Number of neighbors of the current cell
				int neighbors = this.getNbneighbors(this.grid[i][j]);
				
				/* If the square is occupied */
				if(this.grid[i][j].getCellType() != 0) {
					// If there are too many or too few neighbors, free the square at next iteration
					if(neighbors < 2 || neighbors > 3) {
						this.grid[i][j].setNextCellType(0); 
					// Else the next state doesn't change
					} else {
						this.grid[i][j].setNextCellType(1);
					}
				
				/* If the square is empty */
				} else {
					// If there is the proper amount of neighbors
					if(neighbors == 3) {
						this.grid[i][j].setNextCellType(1); 
					} else {
						this.grid[i][j].setNextCellType(0);
					}
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
	 * Method reinitializing the Grid
	 */
	public void reInit() {
		for(int i = 0; i < this.gridSize; i++) {
			for(int j = 0; j < this.gridSize; j++) {
				
				// Copy of the initial grid into the current grid
				this.grid[i][j] = new Cell(this.initGrid[i][j]);
				this.grid[i][j].setNextCellType(this.grid[i][j].getCellType());
			}
		}
	}
	
	/**
	 * Method adding the Grid on a GUISimulator
	 * 
	 * @param gui is the GUISimulator on which to add the Grid
	 */
	public void render(GUISimulator gui) {
		for(int i = 0; i < this.gridSize; i++) {
			for(int j = 0; j < this.gridSize; j++) {
				// Rendering each cell of the grid
				this.grid[i][j].render(gui, this.gridSize);
			}
		}
	}
	
	/**
	 * 
	 * Method finding the number of alive neighbors of a specified cell in the Grid.
	 * 
	 * @param cell is the cell for which we want to find the neighbors
	 * 
	 * @return the number of alive neighbors for the specified cell
	 */
	protected int getNbneighbors(Cell cell) {
		
		Point coo = cell.getCoo();
		int neighbors = 0;
		int lesserX = coo.x - 1;
		int lesserY = coo.y - 1;
		int upperX = coo.x + 1;
		int upperY = coo.y + 1;
		
		/* Adjusting the coordinates of the neighbors, in case the cell is on a border */
		if(lesserX < 0) { lesserX = this.gridSize - 1; }
		if(lesserY < 0) { lesserY = this.gridSize - 1; }
		if(upperX == this.gridSize) { upperX = 0; }
		if(upperY == this.gridSize) { upperY = 0; }
			
		/* Checking the 8 neighbors */
		if(isNeighbor(cell, this.grid[upperX][lesserY])) { neighbors++; }
		if(isNeighbor(cell, this.grid[lesserX][lesserY])) { neighbors++; }
		if(isNeighbor(cell, this.grid[upperX][upperY])) { neighbors++; }
		if(isNeighbor(cell, this.grid[lesserX][upperY])) { neighbors++; }
		if(isNeighbor(cell, this.grid[upperX][coo.y])) { neighbors++; }
		if(isNeighbor(cell, this.grid[lesserX][coo.y])) { neighbors++; }
		if(isNeighbor(cell, this.grid[coo.x][lesserY])) { neighbors++; }
		if(isNeighbor(cell, this.grid[coo.x][upperY])) { neighbors++; }
		
		return neighbors;
	}

	/**
	 * Method checking for a specified cell and a specified neighbor if the neighbor is alive 
	 * 
	 * @param currentCell is the cell to study
	 * @param neighbor is the neighbor to study
	 * 
	 * @return true if the neighbor is alive else false
	 */
	protected boolean isNeighbor(Cell currentCell, Cell neighbor) {
		if(neighbor.getCellType() != 0) { return true; }
		return false;
	}
}
