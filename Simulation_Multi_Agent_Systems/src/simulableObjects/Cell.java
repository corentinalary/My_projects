package simulableObjects;


import java.awt.Color;
import java.awt.Point;
import gui.GUISimulator;
import gui.Rectangle;

/**
 * Class child of SimulableObj representing a cell inside a grid.
 *
 */
public class Cell extends SimulableObj {
	
	static protected Color statesColors[] =  { Color.WHITE, Color.GRAY, Color.DARK_GRAY, Color.BLACK };
	private Point coo;
	private Color cellColor=Color.WHITE;
	private int cellType; // Current cell type
	private int nextCellType; // Cell type at the next iteration
	
	/**
	 * Constructor of the Cell object.
	 * 
	 * @param coo is the coordinates of the cell 
	 * @param cellType is the number representing the state of the cell
	 */
	public Cell(Point coo, int cellType) {
		if(cellType < 0) { throw new IllegalArgumentException("The cell type cannot be negative"); }
		if(coo.x < 0) { throw new IllegalArgumentException("X coordinate out of bounds : the cell must be in array"); }
		if(coo.y < 0) { throw new IllegalArgumentException("Y coordinate out of bounds : the cell must be in array"); }
		
		this.cellType = cellType;
		this.nextCellType = cellType;
		this.cellColor = Cell.statesColors[this.cellType];
		this.coo = coo;
	}
	
	/**
	 * Constructor of the Cell object by copy.
	 * 
	 * @param cell is the Cell object we want to copy.
	 */
	public Cell(Cell cell) {
		this.coo = new Point(cell.coo);
		this.cellType = cell.cellType;
		this.cellColor = cell.cellColor;
	}
	
	/**
	 * Method updating the cell by changing its type and color
	 */
	public void update() {
		this.cellType = this.nextCellType;
		this.cellColor = Cell.statesColors[this.cellType];
	}
	
	/**
	 * Getter
	 * 
	 * @return  the attribute cellType
	 */
	public int getCellType() {
		return this.cellType;
	}
	
	/**
	 * Setter
	 * 
	 * @param cellType is the new value of the attribute 'cellType'
	 */
	public void setNextCellType(int cellType) {
		if(cellType < 0) { throw new IllegalArgumentException("The square type cannot be negative ! "); }
		
		this.nextCellType = cellType;
	}
	
	/**
	 * Method rendering the cell on the specified GUISimulator 
	 * 
	 * @param gui is the GUISimulator on which we want to render the cell
	 * 
	 */
	public void render(GUISimulator gui) {	
		this.render(gui, 30);
	}
	
	/**
	 * Method rendering the cell on the specified GUISimulator
	 * This method adapts the size of a cell to fit the gui size
	 * 
	 * @param gui is the GUISimulator on which we want to render the cell
	 * @param gridSize is the size of the grid (in number of squares per side)
	 * 
	 */
	public void render(GUISimulator gui, int gridSize) {
		int lengthSquare = Math.min(gui.getPanelHeight(), gui.getPanelWidth()) / gridSize;
		Rectangle rectangle = new Rectangle(lengthSquare* (this.coo.x + 1), lengthSquare * (this.coo.y + 1),
				Color.BLACK, this.cellColor, lengthSquare); 
		
		gui.addGraphicalElement(rectangle);
	}

	/**
	 * Getter
	 * 
	 * @return the attribute coo
	 */
	public Point getCoo() {
		return coo;
	}
	
    @Override
    public String toString() {
    	return "Square[" + this.coo.x + ", " + this.coo.y +
    			"|| State : " + this.cellType +
    			"|| Next state : " + this.nextCellType + "]";
    }
}
