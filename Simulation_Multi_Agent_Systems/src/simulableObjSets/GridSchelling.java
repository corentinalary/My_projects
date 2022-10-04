package simulableObjSets;

import java.util.*;

import simulableObjects.Cell;

/**
 * Class child from Grid implementing a grid in the Schelling Game.
 *
 */
public class GridSchelling extends Grid {
	
	private int K;
	private List<Cell> emptyCells = new LinkedList<Cell>();
	
	/**
	 * Constructor of the GridSchelling object
	 * 
	 * @param size is the size of the grid within the GridSchelling object
	 * @param nbColors is the number of colors that can represent a family in total in Schelling game
	 * @param K is the K parameter in the Schelling game.
	 */
	public GridSchelling(int size, int nbColors, int K) {
		super(size, nbColors+1);
		
		if(K < 0) {throw new IllegalArgumentException("K must be a positive constant"); }
		this.K = K;
		
		for(int i = 0; i < this.gridSize; i++) {
			for(int j = 0; j < this.gridSize; j++) {
				if(this.grid[i][j].getCellType() == 0) { this.emptyCells.add(this.grid[i][j]); }
			}
		}
	}
	
	/**
	 * Method updating the grid with the rules of the Schelling game.
	 */
	@Override
	public void update() {	
		
		for(int i = 0; i < this.gridSize; i++) {
			for(int j = 0; j < this.gridSize; j++) {
				
				/* If the square is occupied */
				if(this.grid[i][j].getCellType() != 0) {
					
					// Number of individuals of the same color
					int neighbors = this.getNbneighbors(this.grid[i][j]);
					
					/* If the number of individuals from the same color is too small */
					if( neighbors <= 8-K ) {
						
						/* If there are remaining empty houses */
						if(this.emptyCells.size() != 0) {
							
							// The family will free the house at the next iteration
							this.grid[i][j].setNextCellType(0); 
							
							// The family takes another random empty house at the next iteration
							double randInd = Math.random()*(this.emptyCells.size());
							Cell newCell = this.emptyCells.get((int) randInd);
							
							newCell.setNextCellType(this.grid[i][j].getCellType());
							
							// We remove the new house that is now occupied from the list of empty houses
							this.emptyCells.remove(newCell);
							// We add the previous house to the list of empty houses
							this.emptyCells.add(this.grid[i][j]);
						}
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
	 * Method reinitializing the grid.
	 */
	@Override
	public void reInit() {
		
		/* Copying the initial grid into the current grid */
		for(int i = 0; i < this.gridSize; i++) {
			for(int j = 0; j < this.gridSize; j++) {
				
				this.grid[i][j] = new Cell(this.initGrid[i][j]);
				this.grid[i][j].setNextCellType(this.grid[i][j].getCellType());
			}
		}
		
		/* Reinitializing the list of empty houses */
		this.emptyCells.clear();
		
		for(int i = 0; i < this.gridSize; i++) {
			for(int j = 0; j < this.gridSize; j++) {
				if(this.grid[i][j].getCellType() == 0) { this.emptyCells.add(this.grid[i][j]); }
			}
		}
	}
	
	/**
	 * Method checking for a specified cell and a specified neighbor if the neighbor habitation is vacant
	 * or if the neighbor is in in the same state as the current cell 
	 *
	 * 
	 * @param currentCell is the cell to study
	 * @param neighbor is the neighbor to study
	 * 
	 * @return true if the neighbor habitation is vacant
	 * or if the neighbor is in in the same state else false
	 */
	@Override
	public boolean isNeighbor(Cell currentCell, Cell neighbor) {
		if(neighbor.getCellType() == 0 || currentCell.getCellType() == neighbor.getCellType()) { return true; }
		return false;
	}
}
