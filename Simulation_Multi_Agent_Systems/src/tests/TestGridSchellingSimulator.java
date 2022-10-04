package tests;

import java.awt.Color;
import gui.GUISimulator;
import simulator.GridSchellingSimulator;

public class TestGridSchellingSimulator {
	
	public static void main(String[] args) {
		GUISimulator gui = new GUISimulator(800, 800, Color.BLACK);
		GridSchellingSimulator grid = new GridSchellingSimulator(gui, 50, 3, 5); // grid of size 50x50, with 3 different colors and K=5
		
		gui.setSimulable(grid);
	}
}
