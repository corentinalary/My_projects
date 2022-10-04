package tests;

import java.awt.Color;
import gui.GUISimulator;
import simulator.GridSimulator;


public class TestGridSimulator {

	public static void main(String[] args) {
		GUISimulator gui = new GUISimulator(800, 800, Color.BLACK);
		GridSimulator grid = new GridSimulator(gui, 20); // grid of size 20x20
		
		gui.setSimulable(grid);
	}
}
