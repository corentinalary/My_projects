all: compile_Boids compile_Balls compile_Conway compile_Immigration compile_Schelling



compile_Balls:
	javac -d bin -classpath lib/gui.jar  -sourcepath src src/tests/TestBallsSimulator.java

Balls: compile_Balls
	java -classpath bin:lib/gui.jar tests/TestBallsSimulator


compile_Conway:
	javac -d bin -classpath lib/gui.jar  -sourcepath src src/tests/TestGridSimulator.java

Conway: compile_Conway
	java -classpath bin:lib/gui.jar tests/TestGridSimulator


compile_Immigration:
	javac -d bin -classpath lib/gui.jar  -sourcepath src src/tests/TestGridImmigrationSimulator.java

Immigration: compile_Immigration
	java -classpath bin:lib/gui.jar tests/TestGridImmigrationSimulator


compile_Schelling:
	javac -d bin -classpath lib/gui.jar  -sourcepath src src/tests/TestGridSchellingSimulator.java

Schelling: compile_Schelling
	java -classpath bin:lib/gui.jar tests/TestGridSchellingSimulator


compile_Boids:
	javac -d bin -classpath lib/gui.jar  -sourcepath src src/tests/TestBoidsSimulator.java

Boids: compile_Boids
	java -classpath bin:lib/gui.jar tests/TestBoidsSimulator


clean:
	rm -r bin/*
