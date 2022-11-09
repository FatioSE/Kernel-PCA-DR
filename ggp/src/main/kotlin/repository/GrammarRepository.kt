package repository

import com.google.gson.Gson
import models.Classifier
import models.ClassifierList
import models.GrammarNode
import utils.FileUtils

object GrammarRepository {

    fun loadGrammarTree(grammarPath: S