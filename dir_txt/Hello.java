// package xxx;

public class Hello {

    private String helloText = "Hello, Hexlet!";

    public Hello() {}

    public Hello(String helloText) {
        this.helloText = helloText;
    }

    public String getHello() {
        return helloText;
    }

    public void setHello(String str) {
        helloText = str;
    }

    public String toString() {
        return helloText;
    }

}

