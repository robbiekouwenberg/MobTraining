javac -d bin -cp lib/*.jar src/*.java
java -jar lib/junit-platform-console-standalone-1.10.2.jar --class-path bin --scan-classpath