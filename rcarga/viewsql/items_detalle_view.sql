USE [SBO_EUROLICORES_PRD]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE VIEW [dbo].[items_detalle_view]
as

    SELECT
        T0.DocNum, T1.ItemCode, T2.ItemName, T2.SalFactor2 as 'UxC',
        (T1.Quantity%T2.SalFactor2) AS Und,
        CAST((T1.Quantity/T2.SalFactor2) AS INT) AS Cajas

    FROM
        OINV T0
        INNER JOIN INV1 T1 ON T0.DocEntry = T1.DocEntry
        INNER JOIN OITM T2 ON T1.ItemCode=T2.ItemCode



GO

