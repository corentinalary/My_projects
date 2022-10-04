package tests;

import java.awt.Color;
import gui.GUISimulator;
import simulator.GridImmigrationSimulator;

public class TestGridImmigrationSimulator {
	
	public static void main(String[] args) {
		GUISimulator gui = new GUISimulator(800 , 800 , Color.BLACK);
		GridImmigrationSimulator grid = new GridImmigrationSimulator(gui, 40, 4); // grid of size 40x40 with 4 different states
		
		gui.setSimulable(grid);
	}
}
