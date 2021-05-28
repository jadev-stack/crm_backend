USE [SBO_EUROLICORES_PRD]
GO

/****** Object:  View [dbo].[ItemsFactura]    Script Date: 19/03/2021 15:15:02 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE VIEW [dbo].[ItemsFactura]
as
    SELECT T0.DocNum, T0.CardCode, T0.CardName, convert(decimal(18, 2),T0.DocTotalSy) 'TotalValor', CAST(SUM(ROUND((T1.Quantity / T2.SalFactor2),0,1))as integer) 'Cajas',
        CAST(sum(T1.Quantity % T2.SalFactor2) as integer) 'Unidad'
    FROM OINV T0
        INNER JOIN INV1 T1 ON T0.DocEntry=T1.DocEntry
        INNER JOIN OITM T2 ON T1.ITEMCODE=T2.ITEMCODE
    GROUP BY T0.DOCNUM, T0.CARDCODE, T0.DocTotalSy, T0.DocEntry, T0.CardName
GO


