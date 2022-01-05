An Ecommerce Web Application 

Three major functions 


(High)ProductCatalog --> SQLProductRepository (Low)
(High)Payment Processor --> GooglePayGateway(Low)
                  --> WireTransfer(Low)
(High)CustomerProfile --> (High)Communication (Low)--> EmailSender(Low)
                                  --> VoiceDialer(Low)