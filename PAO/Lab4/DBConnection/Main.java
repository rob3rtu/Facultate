package PAO.Lab4.DBConnection;

public class Main {
    public static void main(String[] args) {
        MySqlDbConnection mySqlDbConnection = new MySqlDbConnection();
        OracleDbConnection oracleDbConnection = new OracleDbConnection();

        mySqlDbConnection.connectToDb();
        oracleDbConnection.connectToDb();

        // DBConnection dbConnection = new MySqlDbConnection();
        // DBConnection dbConnection2 = new OracleDbConnection();
    }
}
