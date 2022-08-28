package core

import models.*
import shared.Artifacts
import kotlin.random.Random

object PopulationFactory {

    fun generateInitialPopulation(): List<Individual> {
        val population = mutableListOf<Individual>()
