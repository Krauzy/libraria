import matplotlib.pyplot as plt
from pandas import DataFrame
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout, SpatialDropout1D, Embedding


class TextSentimentAnalysis:

    def __init__(self, data_frame: DataFrame) -> None:
        data = data_frame
        review_data = data[['text', 'airline_sentiment']]

        self.__data = review_data[review_data['airline_sentiment'] != 'neutral']

        self.__sentimental_label = self.__data.airline_sentiment.factorize()

        self.__tweets = self.__data.text.values

        self.__tokenizer = Tokenizer(num_words=5000)
        self.__tokenizer.fit_on_texts(self.__tweets)

        self.__encoded_docs = self.__tokenizer.texts_to_sequences(self.__tweets)

        self.__padded_sequence = pad_sequences(self.__encoded_docs, maxlen=200)

        self.__embedding_vector_length = 32

        self.__vocab_size = len(self.__tokenizer.word_index) + 1
        self.model = Sequential()
        self.history = None

    def train_model(self) -> None:
        self.model.add(Embedding(self.__vocab_size, self.__embedding_vector_length, input_length=200))
        self.model.add(SpatialDropout1D(0.25))
        self.model.add(LSTM(50, dropout=0.5, recurrent_dropout=0.5))
        self.model.add(Dropout(0.2))
        self.model.add(Dense(1, activation='sigmoid'))

        self.model.compile(
            loss='binary_crossentropy',
            optimizer='adam',
            metrics=['accuracy']
        )

        self.history = self.model.fit(
            x=self.__padded_sequence,
            y=self.__sentimental_label[0],
            validation_split=0.2,
            epochs=5,
            batch_size=32
        )

        self.model.save('/template')

    def plot_accuracy(self) -> plt.Figure:
        fig = plt.figure(figsize=(10, 5))
        plt.plot(self.history.history['accuracy'], label='acc')
        plt.plot(self.history.history['val_accuracy'], label='val_acc')
        plt.legend()
        return fig

    def plot_loss(self):
        fig = plt.figure(figsize=(10, 5))
        plt.plot(self.history.history['loss'], label='loss')
        plt.plot(self.history.history['val_loss'], label='val_loss')
        plt.legend()
        return fig

    def is_positive_sentiment(self, text: str) -> bool:
        tw = self.__tokenizer.texts_to_sequences([text])
        tw = pad_sequences(tw, maxlen=200)
        prediction = int(self.model.predict(tw).round().item())
        return self.__sentimental_label[1][prediction] == 'positive'
