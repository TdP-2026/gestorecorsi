from database.DB_connect import DBConnect


class DAO():

    @staticmethod
    def getCodins(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """
        """

        cursor.execute(query)

        res = []
        for row in cursor:
            pass

        cursor.close()
        cnx.close()
        return res
