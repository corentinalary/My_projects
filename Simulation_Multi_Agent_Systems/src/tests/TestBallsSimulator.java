package tests;

import gui.GUISimulator;
import java.awt.Color;
import simulator.BallsSimulator;

public class TestBallsSimulator {
	public static void main( String [] args ) {
		
		GUISimulator gui = new GUISimulator(750, 550, Color.BLACK);
		BallsSimulator balles = new BallsSimulator(gui);
		
		gui.setSimulable(balles);
	}

}