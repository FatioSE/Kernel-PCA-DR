package cli

import com.github.ajalt.clikt.core.CliktCommand
import com.github.ajalt.clikt.parameters.options.default
import com.github.ajalt.clikt.parameters.options.option
import core.PopulationFactory
import kafka.KafkaController
import models.StreamIndividual
import repository.ConfigurationRepository
import repository.GrammarRepository
import shared.Artifacts
i