package models

import com.google.gson.annotations.SerializedName

data class StreamIndividual(
    var id: String,
    @SerializedName("import_str")
    var 