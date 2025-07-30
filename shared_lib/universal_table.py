from pydantic import BaseModel, Field


class UniversalTable(BaseModel):
    """
    A model representing a universal table with a name and a list of columns.
    """
    name: str = Field(..., description="The name of the table")
    columns: list[str] = Field(..., description="A list of column names in the table")
    
    class Config:
        schema_extra = {
            "example": {
                "name": "users",
                "columns": ["id", "name", "email"]
            }
        }
    def __str__(self):
        return f"UniversalTable(name={self.name}, columns={self.columns})"

    def __repr__(self):
        return f"UniversalTable(name={self.name!r}, columns={self.columns!r})"
    def to_dict(self):
        """
        Convert the UniversalTable instance to a dictionary.
        """
        return {
            "name": self.name,
            "columns": self.columns
        }           
    @classmethod
    def from_dict(cls, data: dict): 
        """
        Create a UniversalTable instance from a dictionary.
        """
        return cls(name=data["name"], columns=data["columns"])
    @classmethod
    def from_list(cls, name: str, columns: list[str]):  
        """
        Create a UniversalTable instance from a list of columns and a name.
        """
        return cls(name=name, columns=columns)

    def add_column(self, column: str):
        """
        Add a column to the table.
        """
        if column not in self.columns:
            self.columns.append(column)
        else:
            raise ValueError(f"Column '{column}' already exists in the table '{self.name}'.")   
    def remove_column(self, column: str):
        """
        Remove a column from the table.
        """
        if column in self.columns:
            self.columns.remove(column)
        else:
            raise ValueError(f"Column '{column}' does not exist in the table '{self.name}'.")
    def has_column(self, column: str) -> bool:
        """
        Check if the table has a specific column.
        """
        return column in self.columns
    def get_columns(self) -> list[str]:
        """
        
        Get the list of columns in the table.
        """
        return self.columns.copy()  
    def rename_table(self, new_name: str):
        """     
        Rename the table.
        """     
        if new_name:
            self.name = new_name
        else:
            raise ValueError("New table name cannot be empty.") 
    def clear_columns(self):
        """
        Clear all columns from the table.
        """
        self.columns.clear()    
 