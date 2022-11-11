package repository

import com.google.gson.Gson
import models.Classifier
import models.ClassifierList
import models.GrammarNode
import utils.FileUtils

object GrammarRepository {

    fun loadGrammarTree(grammarPath: String): GrammarNode {
        val jsonString = FileUtils.readFile(grammarPath)
        val grammarTree = Gson().fromJson(jsonString, GrammarNode::class.java)
        return grammarTree
    }

    fun loadClassifiers(c