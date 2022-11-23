package utils

import java.io.File

object FileUtils {

    fun readFile(fileName: String): String? {
        val file = File(fileName)
        return if (file.exists()) {
            file.readText(Charsets.UT