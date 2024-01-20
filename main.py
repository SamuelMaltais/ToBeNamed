import populationData
import bikeData
import treeData

if __name__ == "__main__":


    ourDictionnary = populationData.getPopulationPerHood()
    bikeData.getBikeData(ourDictionnary)
    treeData.getTreeData(ourDictionnary)

    pass