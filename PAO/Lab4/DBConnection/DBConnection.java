package PAO.Lab4.DBConnection;

public abstract class DBConnection {

    public DBConnection() {
    }

    public abstract void connectToDb();

    public void afterDbConnection() {
        System.out.println("After db connection");
    }
}
