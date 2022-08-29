package core

import models.*
import shared.Artifacts
import kotlin.random.Random

object PopulationFactory {

    fun generateInitialPopulation(): List<Individual> {
        val population = mutableListOf<Individual>()
        repeat(Artifacts.configuration.population) {
            val newIndividual = generateIndividual()
            population.add(newIndividual)
        }

        return population
    }

    fun generateIndividual(): Individual {
        val componentMap: MutableMap<String, IndividualTreeNode>? = mutableMapOf()
        val individualTree = rec