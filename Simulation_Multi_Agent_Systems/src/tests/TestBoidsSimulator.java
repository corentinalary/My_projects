package tests;

import gui.GUISimulator;
import java.awt.Color;
import simulator.BoidsSimulator;

public class TestBoidsSimulator {
	public static void main( String [] args ) {
		
		GUISimulator gui = new GUISimulator(800, 800, Color.BLACK);
		BoidsSimulator boids = new BoidsSimulator(gui);
		
		gui.setSimulable(boids);
	}
}