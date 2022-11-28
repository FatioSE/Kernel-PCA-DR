package models

import org.assertj.core.api.Assertions.assertThat
import org.junit.jupiter.api.Test

class ConfigurationModelTest {

    @Test
    fun configurationDefaultObjectTest() {
        val configuration = Configuration()
        assertThat(confi