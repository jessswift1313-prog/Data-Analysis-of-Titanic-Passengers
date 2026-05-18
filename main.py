import pandas as pd
import matplotlib.pyplot as plt

from data_loader import load_data
from gender import survival_by_gender
from children import survival_by_children
from port import survival_by_port
from cabin import survival_by_class


def section(title):
    print("\n" + "=" * 88)
    print(title)
    print("=" * 88 + "\n")


def main():

    # ==========================================================
    # Load Dataset
    # ==========================================================

    section("1. BASIC INFORMATION")

    titanic = load_data("data/Titanic.csv")

    print(titanic.head())
    print("\nDataset Shape:", titanic.shape)

    # ==========================================================
    # Survival by Gender
    # ==========================================================

    section("2. SURVIVAL RATE BY GENDER")

    survival_by_gender(titanic)

    # ==========================================================
    # Survival by Children / Adults
    # ==========================================================

    section("3. SURVIVAL RATE BY AGE GROUP")

    survival_by_children(titanic)

    # ==========================================================
    # Survival by Embarkation Port
    # ==========================================================

    section("4. SURVIVAL RATE BY EMBARKATION PORT")

    survival_by_port(titanic)

    # ==========================================================
    # Survival by Passenger Class
    # ==========================================================

    section("5. SURVIVAL RATE BY PASSENGER CLASS")

    survival_by_class(titanic)


if __name__ == "__main__":
    main()